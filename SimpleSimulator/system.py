import sys
import matplotlib.pyplot as plt


class MEM:
    def __init__(self, code):
        self.memory = code + ['0000000000000000'] * (256 - len(code))
        self.traces = ([], [])
        self.traces_ldstr = ([], [])

    def dump(self):
        for i in self.memory:
            sys.stdout.write(i + '\n')

    def load(self, ind, cycle):
        if type(ind) == str:
            ind = int(ind, 2)
        if type(ind) == int:
            self.traces_ldstr[0].append(cycle)
            self.traces_ldstr[1].append(ind)
        else:
            self.traces[0].append(cycle)
            self.traces[1].append(int(ind))
        return self.memory[ind]

    def store(self, ind, val, cycle):
        if type(val) == int:
            val = conv_to_bin(val, 16)
        if type(ind) == str:
            ind = int(ind, 2)
        self.memory[ind] = val

        self.traces_ldstr[0].append(cycle)
        self.traces_ldstr[1].append(ind)

    def show_traces(self,save=False):
        plt.scatter(self.traces[0], self.traces[1])
        plt.scatter(self.traces_ldstr[0], self.traces_ldstr[1], color='red')
        plt.title('mem address v/s cycle')
        plt.xlabel('cycle')
        plt.ylabel('address')
        # plt.xlim(0)
        # plt.ylim(0)
        if save:
            plt.savefig("CO_Assignment")
        else:
            plt.show()


class RF:
    def __init__(self):
        self.REG = {'000': '0000000000000000', '001': '0000000000000000', '010': '0000000000000000',
                    '011': '0000000000000000', '100': '0000000000000000', '101': '0000000000000000',
                    '110': '0000000000000000', '111': '0000000000000000'}

    def dump(self):
        for i in self.REG:
            sys.stdout.write(self.REG[i] + ' ')
        sys.stdout.write('\n')

    def get(self, reg):
        return self.REG[reg]

    def set(self, reg, val):
        if type(val) == int:
            if 0 <= val < 2 ** 16:
                val = conv_to_bin(val, 16)
            elif val < 0:
                val = '0000000000000000'
                self.set_flag('V')
            else:
                val = bin(val)[-16:]
                self.set_flag('V')

        else:
            val = '0' * (16 - len(val)) + val
        self.REG[reg] = val

    def set_flag(self, s):
        if s == 'V':  # overflow
            self.REG['111'] = '0' * 12 + '1000'
        elif s == 'L':  # less than
            self.REG['111'] = '0' * 12 + '0100'
        elif s == 'G':  # greater than
            self.REG['111'] = '0' * 12 + '0010'
        elif s == 'E':  # equal
            self.REG['111'] = '0' * 12 + '0001'

    def reset_flag(self):
        self.REG['111'] = '0000000000000000'


class PC:
    def __init__(self, n):
        self.pc = n

    def __index__(self):
        return self.pc

    def __int__(self):
        return self.pc

    def dump(self):
        sys.stdout.write(conv_to_bin(self.pc) + ' ')

    def get(self):
        return self.pc

    def update(self, new_pc):
        if new_pc == -1:
            self.pc += 1
        else:
            self.pc = new_pc


class EE:
    def __init__(self, mem, pc, rf):
        self.mem = mem
        self.pc = pc
        self.rf = rf

    def execute(self, instruction, cycle):
        # return halted,new_pc(-1 if no jump)
        if instruction == '1001100000000000':
            self.rf.reset_flag()
            return True, 0
        opcode = instruction[:5]
        if opcode in ['00000', '00001', '00110', '01010', '01011', '01100']:  # A
            self.rf.reset_flag()
            r1 = instruction[7:10]
            r2 = instruction[10:13]
            r3 = instruction[13:]
            if opcode == '00000':  # addition
                self.rf.set(r1, int(self.rf.get(r2), 2) + int(self.rf.get(r3), 2))
            elif opcode == '00001':  # substraction
                self.rf.set(r1, int(self.rf.get(r2), 2) - int(self.rf.get(r3), 2))
            elif opcode == '00110':  # multiply
                self.rf.set(r1, int(self.rf.get(r2), 2) * int(self.rf.get(r3), 2))
            elif opcode == '01010':  # XOR
                self.rf.set(r1, int(self.rf.get(r2), 2) ^ int(self.rf.get(r3), 2))
            elif opcode == '01011':  # or
                self.rf.set(r1, int(self.rf.get(r2), 2) | int(self.rf.get(r3), 2))
            elif opcode == '01100':  # and
                self.rf.set(r1, int(self.rf.get(r2), 2) & int(self.rf.get(r3), 2))

        elif opcode in ['00010', '01000', '01001']:  # B
            self.rf.reset_flag()
            r1 = instruction[5:8]
            imm = instruction[8:]
            if opcode == '00010':  # move imm
                self.rf.set(r1, '00000000' + imm)
            elif opcode == '01000':  # rs
                self.rf.set(r1, int(self.rf.get(r1), 2) >> imm)
            elif opcode == '01001':  # ls
                self.rf.set(r1, (int(self.rf.get(r1), 2) << imm) % 2 ** 16)

        elif opcode in ['00011', '00111', '01101', '01110']:  # C
            if opcode != '00011':
                self.rf.reset_flag()
            r1 = instruction[10:13]
            r2 = instruction[13:]
            if opcode == '00011':  # move reg
                self.rf.set(r1, self.rf.get(r2))
                self.rf.reset_flag()
            elif opcode == '00111':  # divide
                self.rf.set('000', int(self.rf.get(r1), 2) / int(self.rf.get(r2), 2))
                self.rf.set('001', int(self.rf.get(r1), 2) % int(self.rf.get(r2), 2))
            elif opcode == '01101':  # invert
                self.rf.set(r1, ''.join('1' if i == '0' else '0' for i in self.rf.get(r2)))
            elif opcode == '01110':  # compare
                a, b = int(self.rf.get(r1), 2), int(self.rf.get(r2), 2)
                if a < b:
                    self.rf.set_flag('L')
                elif a > b:
                    self.rf.set_flag('G')
                else:
                    self.rf.set_flag('E')

        elif opcode in ['00100', '00101']:  # D
            self.rf.reset_flag()
            r1 = instruction[5:8]
            mem_addr = instruction[8:]
            if opcode == '00100':  # load
                self.rf.set(r1, self.mem.load(mem_addr), cycle)
            elif opcode == '00101':  # store
                self.mem.store(mem_addr, self.rf.get(r1), cycle)

        else:  # E
            mem_addr = instruction[8:]
            flag = self.rf.get('111')
            if opcode == '01111':
                return False, int(mem_addr, 2)
            elif opcode == '10000':
                if flag[-3] == '1':
                    return False, int(mem_addr, 2)
            elif opcode == '10001':
                if flag[-2] == '1':
                    return False, int(mem_addr, 2)
            elif opcode == '10010':
                if flag[-1] == '1':
                    return False, int(mem_addr, 2)
            self.rf.reset_flag()

        return False, -1


def conv_to_bin(n, length=8):
    b = bin(n)[2:]
    return (length - len(b)) * '0' + b


def conv_to_dec(b):
    return int(b, 2)

# mem ==> 16bit
# reg ==> 16bit
# pc ==>8bit
