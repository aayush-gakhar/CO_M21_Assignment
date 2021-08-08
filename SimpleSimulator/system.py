import sys


class MEM:
    def __init__(self, code):
        self.memory = code + ['0000000000000000'] * (256 - len(code))

    def dump(self):
        # sys.stdout.write('\n')
        for i in self.memory:
            sys.stdout.write(i + '\n')

    def load(self, ind):
        return self.memory[ind]

    def store(self, ind, val):
        if type(val) == int:
            val = conv_to_bin(val)
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
        if type(val)==int:
            if 0<=val<2**16:
                b=bin(val)[2:]
                val='0'*(16-len(b))+b
            else:
                val='0000000000000000'
                self.set_flag('V')
        self.REG[reg] = val

    def set_flag(self, s):
        if s == 'V': # overflow
            self.REG['111'] = '0000000000001000'
        elif s == 'L': # less than
            self.REG['111'] = '0000000000000100'
        elif s == 'G': # greater than
            self.REG['111'] = '0000000000000010'
        elif s == 'E': # equal
            self.REG['111'] = '0000000000000001'

    def reset_flag(self):
        self.REG['111'] = '0000000000000000'


class PC:
    def __init__(self):
        self.pc = 0

    def __index__(self):
        return self.pc

    def dump(self):
        sys.stdout.write(conv_to_bin(self.pc)+' ')

    def get(self):
        return self.pc

    def update(self, new_pc):
        if new_pc == -1:
            self.pc += 1
        else:
            self.pc = new_pc


def execute(instruction, a):
    # return halted,new_pc(-1 if no jump)
    if instruction == '1001100000000000':
        return True, 0
    mem, pc, rf = a
    opcode = instruction[:5]
    if opcode in ['00000', '00001', '00110', '01010', '01011', '01100']:  # A
        rf.reset_flag()
        r1 = instruction[7:10]
        r2 = instruction[10:13]
        r3 = instruction[13:]
        if opcode == '00000':  # addition
            rf.set(r1, int(rf.get(r2), 2) + int(rf.get(r2), 2))
        elif opcode == '00001':  # substraction
            rf.set(r1, int(rf.get(r2), 2) - int(rf.get(r2), 2))
        elif opcode == '00110':  # multiply
            rf.set(r1, int(rf.get(r2), 2) * int(rf.get(r2), 2))
        elif opcode == '01010':  # XOR
            rf.set(r1, int(rf.get(r2), 2) ^ int(rf.get(r2), 2))
        elif opcode == '01011':  # or
            rf.set(r1, int(rf.get(r2), 2) & int(rf.get(r2), 2))
        elif opcode == '01100':  # and
            rf.set(r1, int(rf.get(r2), 2) | int(rf.get(r2), 2))

    elif opcode in ['00010', '01000', '01001']:  # B
        if opcode == '00010':
            pass
        elif opcode == '01000':
            pass
        elif opcode == '01001':
            pass

    elif opcode in ['00011', '00111', '01101', '01110']:  # C
        if opcode == '00011':
            pass
        elif opcode == '00111':
            pass
        elif opcode == '01101':
            pass
        elif opcode == '01110':
            pass

    elif opcode in ['00100', '00101']:  # D
        if opcode == '00100':
            pass
        elif opcode == '00101':
            pass

    else:  # E
        if opcode == '01111':
            pass
        elif opcode == '10000':
            pass
        elif opcode == '10001':
            pass
        elif opcode == '10010':
            pass

    return False, -1


def conv_to_bin(n):
    b = bin(n)[2:]
    return (8 - len(b)) * '0' + b


def conv_to_dec(b):
    return int(b, 2)


def run(code):
    mem = MEM(code)
    pc = PC()
    rf = RF()
    halted = False
    a = [mem, pc, rf]
    while not halted:
        Instruction = mem.load(pc)
        halted, new_pc = execute(Instruction, a)
        pc.dump()
        rf.dump()
        pc.update(new_pc)
    mem.dump()


reg_codes = {'R0': '000', 'R1': '001', 'R2': '010', 'R3': '011', 'R4': '100', 'R5': '101',
             'R6': '110', 'FLAGS': '111'}

# mem ==> 16bit
# reg ==> 16bit
# pc ==>8bit
