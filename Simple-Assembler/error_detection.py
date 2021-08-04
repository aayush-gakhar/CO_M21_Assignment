import sys


def check(code):
    # return True if error in code !!!
    return halt_check(code) or iterate(code)


def iterate(code):
    var_flag = True
    for line_no, line in enumerate(code, start=1):
        line = line.split()
        if not line:
            continue
        elif line[0] == 'var' and not var_flag:
            'VarInMidError'
        elif var_flag and line[0] == 'var':
            return variable_check(line, line_no)
        elif line[0][-1] == ':':
            var_flag = False
            return label_check(line, line_no) and instruction_check(line[1:], line_no)
        elif line[0] in Instructions:
            var_flag = False
            return instruction_check(line, line_no)
        else:
            raise_error(0, line_no)
            return False


def variable_check(line, line_no):
    return len(line) == 2 and all(i in '_0123456789abcdefghijklmnopqrstuvwxyz' for i in line[1].lower())


def instruction_check(line, line_no):
    if line[0] not in Instructions:
        raise_error(0, line_no)
        return False


def label_check(line, line_no):
    'LabelError'


def halt_check(code):
    try:
        f = [i for i in code].index('hlt')
        if f != len(code) - 1:
            raise_error(8, f)
            return True
        else:
            return False
    except ValueError:
        raise_error(7, len(code - 1))
        return True


def raise_error(error, line_no):
    error_flag = True
    sys.stdout.write(errors[error] + ' Line: ' + line_no)


Instructions = ['add', 'sub', 'mov', 'ld', 'st', 'mul', 'div', 'rs', 'ls', 'xor', 'or', 'and', 'not', 'cmp', 'jmp',
                'jlt', 'jgt', 'je', 'hlt']
error_flag = False
errors = ['NameError', 'VariableError', 'LabelError', 'FlagError', 'ImmediateError', 'MisuseError', 'VarInMidError',
          'MissingHltError', 'HltInMidError', 'SyntaxError', 'GeneralSyntaxError']
