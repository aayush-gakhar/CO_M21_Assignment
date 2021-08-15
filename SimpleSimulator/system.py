import sys
import matplotlib.pyplot as plt


class MEM:
    def __init__(self, code):
        self.memory = code + ['0000000000000000'] * (256 - len(code))

    def dump(self):
        for i in self.memory:
            sys.stdout.write(i + '\n')

    def load(self, ind):
        if type(ind) == str:
            ind = conv_to_dec(ind)
        return self.memory[ind]

    def store(self, ind, val):
        if type(val) == int:
            val = conv_to_bin(val, 16)
        if type(ind) == str:
            ind = conv_to_dec(ind)
        self.memory[ind] = val


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
                val=conv_to_bin(val,16)
            else:
                val = '0000000000000000'
                self.set_flag('V')
        else:
            val='0'*(16-len(val))+val
        self.REG[reg] = val

    def set_flag(self, s):
        if s == 'V':  # overflow
            self.REG['111'] = '0'*12+'1000'
        elif s == 'L':  # less than
            self.REG['111'] = '0'*12+'0100'
        elif s == 'G':  # greater than
            self.REG['111'] = '0'*12+'0010'
        elif s == 'E':  # equal
            self.REG['111'] = '0'*12+'0001'

    def reset_flag(self):
        self.REG['111'] = '0000000000000000'


class PC:
    def __init__(self):
        self.pc = 0

    def __index__(self):
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


def execute(instruction, a):
    # return halted,new_pc(-1 if no jump)
    mem, pc, rf = a
    if instruction == '1001100000000000':
        rf.reset_flag()
        return True, 0
    opcode = instruction[:5]
    if opcode in ['00000', '00001', '00110', '01010', '01011', '01100']:  # A
        rf.reset_flag()
        r1 = instruction[7:10]
        r2 = instruction[10:13]
        r3 = instruction[13:]
        if opcode == '00000':  # addition
            rf.set(r1, int(rf.get(r2), 2) + int(rf.get(r3), 2))
        elif opcode == '00001':  # substraction
            rf.set(r1, int(rf.get(r2), 2) - int(rf.get(r3), 2))
        elif opcode == '00110':  # multiply
            rf.set(r1, int(rf.get(r2), 2) * int(rf.get(r3), 2))
        elif opcode == '01010':  # XOR
            rf.set(r1, int(rf.get(r2), 2) ^ int(rf.get(r3), 2))
        elif opcode == '01011':  # or
            rf.set(r1, int(rf.get(r2), 2) | int(rf.get(r3), 2))
        elif opcode == '01100':  # and
            rf.set(r1, int(rf.get(r2), 2) & int(rf.get(r3), 2))

    elif opcode in ['00010', '01000', '01001']:  # B
        rf.reset_flag()
        r1 = instruction[5:8]
        imm = instruction[8:]
        if opcode == '00010':  # move imm
            rf.set(r1, '00000000' + imm)
        elif opcode == '01000':  # rs
            rf.set(r1, int(rf.get(r1), 2) >> imm)
        elif opcode == '01001':  # ls
            rf.set(r1, (int(rf.get(r1), 2) << imm) % 2 ** 16)

    elif opcode in ['00011', '00111', '01101', '01110']:  # C
        if opcode != '00011':
            rf.reset_flag()
        r1 = instruction[10:13]
        r2 = instruction[13:]
        if opcode == '00011':  # move reg
            rf.set(r1, rf.get(r2))
            rf.reset_flag()
        elif opcode == '00111':  # divide
            rf.set('000', int(rf.get(r1), 2) / int(rf.get(r2), 2))
            rf.set('001', int(rf.get(r1), 2) % int(rf.get(r2), 2))
        elif opcode == '01101':  # invert
            rf.set(r1, ''.join('1' if i == '0' else '0' for i in rf.get(r2)))
        elif opcode == '01110':  # compare
            a, b = int(rf.get(r1), 2), int(rf.get(r2), 2)
            if a < b:
                rf.set_flag('L')
            elif a > b:
                rf.set_flag('G')
            else:
                rf.set_flag('E')

    elif opcode in ['00100', '00101']:  # D
        rf.reset_flag()
        r1 = instruction[5:8]
        mem_addr = instruction[8:]
        if opcode == '00100':  # load
            rf.set(r1, mem.load(mem_addr))
        elif opcode == '00101':  # store
            mem.store(mem_addr, rf.get(r1))

    else:  # E
        mem_addr = instruction[8:]
        flag = rf.get('111')
        if opcode == '01111':
            return False, conv_to_dec(mem_addr)
        elif opcode == '10000':
            if flag[-3] == '1':
                return False, conv_to_dec(mem_addr)
        elif opcode == '10001':
            if flag[-2] == '1':
                return False, conv_to_dec(mem_addr)
        elif opcode == '10010':
            if flag[-1] == '1':
                return False, conv_to_dec(mem_addr)
        rf.reset_flag()

    return False, -1


def conv_to_bin(n, l=8):
    b = bin(n)[2:]
    return (l - len(b)) * '0' + b


def conv_to_dec(b):
    return int(b, 2)


def run(code, scatter=False):
    mem = MEM(code)
    pc = PC()
    rf = RF()
    addr = []
    halted = False
    a = [mem, pc, rf]
    while not halted:
        addr.append(pc.get())
        Instruction = mem.load(pc)
        halted, new_pc = execute(Instruction, a)
        pc.dump()
        rf.dump()
        pc.update(new_pc)
    mem.dump()
    if scatter:
        plt.scatter([i + 1 for i in range(len(addr))], addr, s=5, cmap='viridis')
        plt.show()


# mem ==> 16bit
# reg ==> 16bit
# pc ==>8bit
