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
    b = len(line) != 2 or any(i not in '_0123456789abcdefghijklmnopqrstuvwxyz' for i in line[1].lower()) or line[
        1] in var
    var.add(line[1])
    if b:
        raise_error(1, line_no)
    return b


def instruction_check(line, line_no):
    if line[0] not in Instructions:
        raise_error(0, line_no)
        return False


def label_check(line, line_no):
    lname = line[0][:-1]
    b = line[-1] != ':' or any(i not in '_0123456789abcdefghijklmnopqrstuvwxyz' for i in lname.lower()) or lname in \
        labels or lname < 1
    labels.add(lname)
    if b:
        raise_error(2,line_no)
    return b


def halt_check(code):
    try:
        code = [i for i in code if i]
        print(code)
        f = code.index('hlt\n')
        if f != len(code) - 1:
            raise_error(8, f)
            return True
        else:
            return False
    except ValueError:
        if code[-1]=='hlt':
            return False
        raise_error(7, len(code) - 1)
        return True


def raise_error(error, line_no):
    error_flag = True
    sys.stdout.write(errors[error] + ' Line: ' + str(line_no) + '\n')


Instructions = ['add', 'sub', 'mov', 'ld', 'st', 'mul', 'div', 'rs', 'ls', 'xor', 'or', 'and', 'not', 'cmp', 'jmp',
                'jlt', 'jgt', 'je', 'hlt']
error_flag = False
errors = ['NameError', 'VariableError', 'LabelError', 'FlagError', 'ImmediateError', 'MisuseError', 'VarInMidError',
          'MissingHltError', 'HltInMidError', 'SyntaxError', 'GeneralSyntaxError']
var = set()
labels = set()
