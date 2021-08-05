import sys


def compile(code):
    for line in code:
        if not line:
            continue
        elif line.split()[0] == 'var':
            compile_variable(line)
        elif line.split()[0] in Instructions:
            compile_instruction(line)
        elif line.split()[0][-1] == ':':
            compile_label(line)


def compile_variable(line):
    pass


def compile_label(line):
    pass


def compile_instruction(line):
    if line.split()[0] == 'add':
        opcode = '00000'

    elif line.split()[0] == 'sub':
        opcode = '00001'

    elif line.split()[0] == 'mov':

        if line.split()[2][0]=='$':
            opcode = '00010'

        else:
            opcode='00011'

    elif line.split()[0] == 'ld':
        opcode = '00100'

    elif line.split()[0] == 'st':
        opcode = '00101'

    elif line.split()[0] == 'mul':
        opcode = '00110'

    elif line.split()[0] == 'div':
        opcode = '00111'

    elif line.split()[0] == 'rs':
        opcode = '01000'

    elif line.split()[0] == 'ls':
        opcode = '01001'

    elif line.split()[0] == 'xor':
        opcode = '01010'

    elif line.split()[0] == 'or':
        opcode = '01011'

    elif line.split()[0] == 'and':
        opcode = '01100'

    elif line.split()[0] == 'not':
        opcode = '01101'

    elif line.split()[0] == 'cmp':
        opcode = '01110'

    elif line.split()[0] == 'jmp':
        opcode = '01111'

    elif line.split()[0] == 'jlt':
        opcode = '10000'

    elif line.split()[0] == 'jgt':
        opcode = '10001'

    elif line.split()[0] == 'je':
        opcode = '10010'

    elif line.split()[0] == 'hlt':
        opcode = '10011'


Instructions = ['add', 'sub', 'mov', 'ld', 'st', 'mul', 'div', 'rs', 'ls', 'xor', 'or', 'and', 'not', 'cmp', 'jmp',
                'jlt', 'jgt', 'je', 'hlt']

Reg = [['R0', '000'], ['R1', '001'], ['R2', '010'], ['R3', '011'], ['R4', '100'], ['R5', '101'], ['R6', '110']]
