import sys


def compile(code):
    i = 0
    for line in code:
        line=line.split()
        if not line:
            continue
        elif line[0] == 'var':
            compile_variable(line)
        elif line[0] in Instructions:
            compile_instruction(line)
        elif line[0][-1] == ':':
            compile_label(line,i)
        i+=1



def compile_variable(line):

    pass


def compile_label(line , i):
    label_dict[line[0][:-1]] = i
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


    elif line[0] in ['div','not','cmp',]:
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

label_dict={}

Instructions = {'add':'00000', 'sub':'00001', 'mov':'00010', 'ld':'00100','st':'00101', 'mul':'00110', 'div':'00111', 'rs':'01000', 'ls':'01001', 'xor':'01010', 'or':'01011', 'and':'01100', 'not':'01101', 'cmp':'01110', 'jmp':'01111',
                'jlt':'10000', 'jgt':'10001', 'je':'10010', 'hlt':'10011'}

Reg = {'R0':'000', 'R1':'001', 'R2': '010', 'R3': '011', 'R4': '100', 'R5': '101',
       'R6':'110'}
