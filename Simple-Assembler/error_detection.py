import sys


def check(code):
    return halt_check(code) and typo(code)


def typo(code):
    for line in code:
        line = line.split()
        if not line:
            continue
        elif line[0] == 'var':
            return variable_check(line)
        elif line[0][-1] == ':':
            return label_check(line) and instruction_check(line[1:])
        elif line[0] in Instructions:
            return instruction_check(line)


def variable_check(line):
    pass


def instruction_check(line):
    pass


def label_check(line):
    pass


def halt_check(code):
    f = code.find('hlt')
    if f==-1:
        'MissingHltError'
    elif f!=len(code)-1:
        'HltInMidError'
    else:
        return True


def raise_error(error, line_no):
    error_flag = True
    sys.stdout.write(errors[error] + ' Line: ' + line_no)


Instructions = ['add', 'sub', 'mov', 'ld', 'st', 'mul', 'div', 'rs', 'ls', 'xor', 'or', 'and', 'not', 'cmp', 'jmp',
                'jlt', 'jgt', 'je', 'hlt']
error_flag = False
errors = ['NameError', 'VariableError', 'LabelError', 'FlagError', 'ImmediateError', 'MisuseError', 'VarInMidError',
          'MissingHltError', 'HltInMidError', 'SyntaxError', 'GeneralSyntaxError']
