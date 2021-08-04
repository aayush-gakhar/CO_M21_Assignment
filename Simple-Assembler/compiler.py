def compile(code):
    for line in code:
        if not line:
            continue
        elif line.split()[0] =='var':
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
    pass


Instructions = ['add', 'sub', 'mov', 'ld', 'st', 'mul', 'div', 'rs', 'ls', 'xor', 'or', 'and', 'not', 'cmp', 'jmp',
                'jlt', 'jgt', 'je', 'hlt']