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
        pass

    def set(self,reg,val):
        pass


class PC:
    def __init__(self):
        self.pc = 0

    def dump(self):
        sys.stdout.write(conv_to_bin(self.pc))

    def get(self):
        return self.pc

    def update(self,new_pc):
        if new_pc==-1:
            self.pc+=1
        else:
            self.pc=new_pc

def execute(instruction, a):
    # return halted,new_pc(-1 if no jump)
    if instruction == '1001100000000000':
        return True, 0
    mem, pc, rf = a
    opcode=instruction[:5]
    if opcode in ['00000','00001','00110','01010','01011','01100']: # A
        r1 = instruction[7:10]
        r2 = instruction[10:13]
        r3 = instruction[13:]
        if opcode=='00000':
            rf
        elif opcode=='00001':
            pass
        elif opcode == '00110':
            pass
        elif opcode == '01010':
            pass
        elif opcode == '01011':
            pass
        elif opcode == '01100':
            pass

    elif opcode in ['00010','01000','01001']: # B
        if opcode == '00010':
            pass
        elif opcode == '01000':
            pass
        elif opcode == '01001':
            pass

    elif opcode in ['00011','00111','01101','01110']: # C
        if opcode == '00011':
            pass
        elif opcode == '00111':
            pass
        elif opcode == '01101':
            pass
        elif opcode == '01110':
            pass

    elif opcode in ['00100','00101']: # D
        if opcode == '00100':
            pass
        elif opcode == '00101':
            pass

    else: # E
        if opcode == '01111':
            pass
        elif opcode == '10000':
            pass
        elif opcode == '10001':
            pass
        elif opcode == '10010':
            pass


class EE:
    pass


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
        halted, new_pc = execute(Instruction,a)
        pc.dump()
        rf.dump()
        pc.update(new_pc)
    mem.dump()
