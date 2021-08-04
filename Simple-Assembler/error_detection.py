import sys


def check(code):
    return halt_check(code) and typo(code)


def typo(code):
    var_flag=True
    for line in code:
        line = line.split()
        if not line:
            continue
        elif line[0] == 'var' and not var_flag:
            'VarInMidError'
        elif var_flag and line[0] == 'var':
            return variable_check(line)
        elif line[0][-1] == ':':
            var_flag=False
            return label_check(line) and instruction_check(line[1:])
        elif line[0] in Instructions:
            var_flag=False
            return instruction_check(line)
        else:
            'NameError'


def variable_check(line):
    'VariableError'


def instruction_check(line):
    'NameError'


def label_check(line):
    'LabelError'


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
