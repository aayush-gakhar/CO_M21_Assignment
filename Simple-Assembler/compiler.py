import sys


def compile(code):
    for line in code:
        line=line.split()
        if not line:
            continue
        elif line[0] == 'var':
            compile_variable(line)
        elif line[0] in Instructions:
            compile_instruction(line)
        elif line[0][-1] == ':':
            compile_label(line)



def compile_variable(line):
    pass


def compile_label(line):
    pass


def compile_instruction(line):


    if line[0] in ['add','sub','mul','xor','or','and',]:
        opcode = Instructions[line[0]]
        reg1 = Reg[int(line[1][1])][1]
        reg2 = Reg[int(line[2][1])][1]
        reg3 = Reg[int(line[3][1])][1]
        sys.stdout.write(opcode+2*'0'+reg1+reg2+reg3)
        sys.stdout.write('\n')



    elif line[0] in ['rs','ls']:
        opcode = Instructions[line[0]]
        reg1 = Reg[int(line[1][1])][1]
        reg2 = Reg[int(line[2][1])][1]
        reg3 = Reg[int(line[3][1])][1]
        sys.stdout.write(opcode + 2 * '0' + reg1 + reg2 + reg3)
        sys.stdout.write('\n')

# <<<<<<< HEAD
        Reg[int(line.split()[1][1])][2] = Reg[int(line.split()[2][1])][2] * Reg[int(line.split()[3][1])][2]

    elif line.split()[0] == 'div':
        opcode = '00111'
        reg1 = Reg[int(line.split()[1][1])][1]
        reg2 = Reg[int(line.split()[2][1])][1]
        sys.stdout.write(opcode + 5 * '0' + reg1 + reg2)
        sys.stdout.write('\n')


    elif line.split()[0] == 'rs':
        opcode = '01000'
        imm = str(bin(int(line.split()[2][1:]))[2:])
        reg1=Reg[int(line.split()[1][1])][1]
        un=(8-len(imm))
        sys.stdout.write(opcode + reg + un * '0' + imm)
        sys.stdout.write('\n')
        Reg[int(line.split()[1][1])][2]=int(line.split()[2][1:])  #inputting the value to that register

    elif line.split()[0] == 'ls':
        opcode = '01001'
        imm = str(bin(int(line.split()[2][1:]))[2:])
        reg1=Reg[int(line.split()[1][1])][1]
        un=(8-len(imm))
        sys.stdout.write(opcode + reg + un * '0' + imm)
        sys.stdout.write('\n')
        Reg[int(line.split()[1][1])][2]=int(line.split()[2][1:])  #inputting the value to that register
# =======
    elif line[0] in ['div','not','cmp',]:
# >>>>>>> 7ff1506046bbc3a56a6604e8a6af1f9657fef699

        opcode = Instructions[line[0]]
        reg1 = Reg[int(line[1][1])][1]
        reg2 = Reg[int(line[2][1])][1]
        un=5
        sys.stdout.write(opcode + un*'0'+ reg1 + reg2)
        sys.stdout.write('\n')


    elif line[0] in ['ld','st',]:
        opcode = Instructions[line[0]]

    elif line[0] in ['jlt','jgt','jmp','je']:
        opcode = Instructions[line[0]]


    elif line[0] == 'hlt':
        opcode = Instructions[line[0]]
        sys.stdout.write(opcode+11*'0')
        sys.stdout.write('\n')

    elif line[0] == 'mov':
        opcode = Instructions[line[0]]
        sys.stdout.write()
        sys.stdout.write('\n')


Instructions = {'add':'00000', 'sub':'00001', 'mov':'00010', 'ld':'00100','st':'00101', 'mul':'00110', 'div':'00111', 'rs':'01000', 'ls':'01001', 'xor':'01010', 'or':'01011', 'and':'01100', 'not':'01101', 'cmp':'01110', 'jmp':'01111',
                'jlt':'10000', 'jgt':'10001', 'je':'10010', 'hlt':'10011'}

Reg = {'R0':'000', 'R1':'001', 'R2': '010', 'R3': '011', 'R4': '100', 'R5': '101',
       'R6':'110'}

