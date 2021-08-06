import sys


def compile_(code, ins_no, l, v):
    global labels
    labels = l
    global variables
    variables = v
    instruction_number[0] = ins_no
    i = 0
    for line in code:
        if not line:
            continue
        elif line[0] == 'var':
            compile_variable(line)
        elif line[0] in Instructions:
            compile_instruction(line)
        elif line[0][-1] == ':':
            compile_instruction(line[1:])


def compile_variable(line):
    variables[line[1]] = conv_bin(instruction_number[0])
    instruction_number[0] += 1


def compile_instruction(line):
    if line[0] in ['add', 'sub', 'mul', 'xor', 'or', 'and', ]:
        sys.stdout.write(Instructions[line[0]] + 2 * '0' + Reg[line[1]] + Reg[line[2]] + Reg[line[3]] + '\n')

    elif line[0] in ['rs', 'ls']:
        sys.stdout.write(Instructions[line[0]] + Reg[line[1]] + conv_bin(line[2][1:]) + '\n')

    elif line[0] in ['div', 'not', 'cmp']:
        sys.stdout.write(Instructions[line[0]] + 5 * '0' + Reg[line[1]] + Reg[line[2]] + '\n')

    elif line[0] in ['ld', 'st']:
        opcode = Instructions[line[0]]
        sys.stdout.write(Instructions[line[0]]+Reg[line[1]]+variables[line[2]]+'\n')

    elif line[0] in ['jlt', 'jgt', 'jmp', 'je']:
        sys.stdout.write(Instructions[line[0]] + '000' + conv_bin(labels[line[1]]) + '\n')

    elif line[0] == 'hlt':
        sys.stdout.write(Instructions[line[0]] + 11 * '0' )

    elif line[0] == 'mov':
        if line[2][0] == '$':
            sys.stdout.write('00010' + Reg[line[1]] + conv_bin(line[2][1:]) + '\n')
        else:
            sys.stdout.write('00011' + 5 * '0' + Reg[line[1]] + Reg[line[2]] + '\n')


def conv_bin(n):
    l = 8
    s = bin(int(n)).replace('0b', '')
    return (8 - len(s)) * '0' + s


Instructions = {'add': '00000', 'sub': '00001', 'mov': '00010', 'ld': '00100', 'st': '00101', 'mul': '00110',
                'div': '00111', 'rs': '01000', 'ls': '01001', 'xor': '01010', 'or': '01011', 'and': '01100',
                'not': '01101', 'cmp': '01110', 'jmp': '01111',
                'jlt': '10000', 'jgt': '10001', 'je': '10010', 'hlt': '10011'}

Reg = {'R0': '000', 'R1': '001', 'R2': '010', 'R3': '011', 'R4': '100', 'R5': '101',
       'R6': '110', 'FLAGS': '111'}
variables = {}
labels = {}
instruction_number = [0]
