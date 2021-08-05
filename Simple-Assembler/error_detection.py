import sys


def check(code):
    # return True if error in code !!!

    return halt_check(code) or iterate(code), var, labels


def iterate(code):
    var_flag = True
    for line_no, line in enumerate(code, start=1):
        print(line)
        if not line:
            continue
        elif line[0] == 'var':
            if var_flag:
                if variable_check(line, line_no):
                    return True
            else:
                raise_error(6, line_no)
                return True
        elif line[0][-1] == ':':
            var_flag = False
            if label_check(line, line_no) and instruction_check(line[1:], line_no):
                return True
        elif line[0] in Instructions:
            var_flag = False
            if instruction_check(line, line_no):
                return True
        else:
            raise_error(0, line_no)
            return True


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
    if line[0] in ['add', 'sub', 'mul']:
        if len(line) == 4 and all(i in reg for i in line[1:]):
            return False
        else:
            raise_error(9, line_no)
            return True
    elif line[0] == 'mov':
        if len(line) == 3 and line[1] in reg and (line[2] in reg or immediate_check(line[2], line_no)):
            return False
        else:
            raise_error(9, line_no)
            return True
    elif line[0] in ['ld', 'st']:
        if len(line) == 3 and line[1] in reg and line[2] in var:
            return False
        else:
            raise_error(9, line_no)
            return True
    elif line[0] in ['rs', 'ls']:
        if len(line) == 3 and line[1] in reg and immediate_check(line[2], line_no):
            return False
        else:
            raise_error(9, line_no)
            return True
    elif line[0] in ['xor', 'or', 'and']:
        if len(line == 4) and all(i in reg for i in line[1:]):
            return False
        else:
            raise_error(9, line_no)
            return True
    elif line[0] in ['div', 'not', 'cmp']:
        if len(line == 3) and all(i in reg for i in line[1:]):
            return False
        else:
            raise_error(9, line_no)
            return True
    elif line[0] in ['jmp', 'jlt', 'jgt', 'je']:
        if len(line == 2) and line[1] in labels:
            return False
        else:
            raise_error(9, line_no)
            return True
    elif line == ['hlt']:
        return False
    else:
        raise_error(9,line_no)
        return True


# def reg_check(reg,line_no):


def immediate_check(imm, line_no):
    if imm[0] == '$':
        try:
            return not 0 <= int(imm[1:]) <= 255
        except:
            raise_error(4, line_no)
            return True
    else:
        raise_error(4, line_no)
        return True


def label_check(line, line_no):
    lname = line[0][:-1]
    b = line[-1] != ':' or any(i not in '_0123456789abcdefghijklmnopqrstuvwxyz' for i in lname.lower()) or lname in labels or lname < 1
    labels.add(lname)
    if b:
        raise_error(2, line_no)
    return b


def halt_check(code):
    # done
    x = len(code) - 1
    while x >= 0:
        if not code[x]:
            code.pop(x)
            x -= 1
        else:
            break
    if x == -1:
        raise_error(7, 0)
        return True
    for line_no, line in enumerate(code[:-1], 1):
        if line[0] == 'hlt':
            raise_error(8, line_no)
            return True
    if code[-1]==['hlt']:
        return False
    else:
        raise_error(7, x)
        return True


def raise_error(error, line_no):
    error_flag = True
    sys.stdout.write(errors[error] + ' Line: ' + str(line_no) + '\n')


Instructions = ['add', 'sub', 'mov', 'ld', 'st', 'mul', 'div', 'rs', 'ls', 'xor', 'or', 'and', 'not', 'cmp', 'jmp',
                'jlt', 'jgt', 'je', 'hlt']
error_flag = False
errors = ['NameError', 'VariableError', 'LabelError', 'FlagError', 'ImmediateError', 'MisuseError', 'VarInMidError',
          'MissingHltError', 'HltInMidError', 'SyntaxError', 'GeneralSyntaxError']
reg = ['R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6']
var = set()
labels = set()
ins_number=0
