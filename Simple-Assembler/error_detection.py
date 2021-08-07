import sys


def check(code):
    # return True if error in code !!!

    b = halt_check(code)  or iterate(code)
    x = [i for i in used if i not in labels]
    if x:
        raise_error(2,used[x[0]],x[0])

    return b or x, var, labels, instruction_number[0]



def iterate(code):
    var_flag = True
    for line_no, line in enumerate(code, start=1):
        # print(line)
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
            if label_check(line, line_no) or instruction_check(line[1:], line_no):
                return True
            code[line_no-1]=line[1:]
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
    var[line[1]] = ''
    if b:
        raise_error(1, line_no)
    return b


def instruction_check(line, line_no):
    if line[0] not in Instructions:
        raise_error(0, line_no)
        return True
    else:
        instruction_number[0] += 1
    if line[0] in ['add', 'sub', 'mul', 'xor', 'or', 'and']:
        if len(line) == 4:
            if all(i in reg for i in line[1:]):
                return False
            elif 'FLAGS' in line:
                raise_error(3,line_no)
                return True
            else:
                raise_error(0,line_no)
                return True
        else:
            raise_error(9, line_no)
            return True
    elif line[0] == 'mov':
        if len(line) == 3:
            if line[1] in reg:
                if line[2] in reg or line[2] == 'FLAGS':
                    return False
                elif line[2][0]=='$':
                    return immediate_check(line[2], line_no)
                else:
                    raise_error(0,line_no)
                    return True
            else:
                raise_error(0,line_no,line[1])
        else:
            raise_error(9, line_no)
            return True
    elif line[0] in ['ld', 'st']:
        if len(line) == 3:
            if line[1] in reg and line[2] in var:
                return False
            elif line[2] not in var:
                raise_error(1,line_no)
                return True
            elif line[1] == 'FLAGS':
                raise_error(3,line_no)
                return True
        else:
            raise_error(9, line_no)
            return True
    elif line[0] in ['rs', 'ls']:
        if len(line) == 3:
            if line[1] in reg:
                return immediate_check(line[2], line_no)
            else:
                raise_error(0,line_no,line[1])
        else:
            raise_error(9, line_no,line)
            return True
    elif line[0] in ['div', 'not', 'cmp']:
        if len(line) == 3:
            if all(i in reg for i in line[1:]):
                return False
            elif 'FLAGS' in line:
                raise_error(3, line_no)
                return True
            else:
                raise_error(0, line_no)
                return True
        else:
            raise_error(9, line_no)
            return True
    elif line[0] in ['jmp', 'jlt', 'jgt', 'je']:
        if len(line)==2:
            if line[1] not in labels and line[1] not in used:
                if line[1] in var:
                    raise_error(5,line_no)
                    return True
                used[line[1]]=line_no
            return False
        else:
            raise_error(9, line_no)
            return True
    elif line == ['hlt']:
        return False
    else:
        raise_error(9, line_no)
        return True
    raise_error(9,line_no)
    return True


# def reg_check(reg,line_no):


def immediate_check(imm, line_no):
    if imm[0] == '$':
        try:
            if 0 <= int(imm[1:]) <= 255:
                return False
            else:
                raise_error(4, line_no,imm)
                return True
        except:
            raise_error(4, line_no)
            return True
    else:
        raise_error(4, line_no)
        return True


def label_check(line, line_no):
    lname = line[0][:-1]
    b = line[0][-1] != ':' or any(
        i not in '_0123456789abcdefghijklmnopqrstuvwxyz' for i in lname.lower()) or lname in labels or len(lname) < 1
    labels[lname] = instruction_number[0]
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
        if not line:
            continue
        if 'hlt' in line:
            raise_error(8, line_no)
            return True
    if 'hlt' in code[-1]:
        return False
    else:
        raise_error(7, x)
        return True


def raise_error(error, line_no,s=''):
    error_flag = True
    sys.stdout.write('ERROR: '+errors[error] + '; Line: ' + str(line_no)+(' ==>' if s else '') + s + '\n')


Instructions = ['add', 'sub', 'mov', 'ld', 'st', 'mul', 'div', 'rs', 'ls', 'xor', 'or', 'and', 'not', 'cmp', 'jmp',
                'jlt', 'jgt', 'je', 'hlt']
error_flag = False
errors = ['Typo Error', 'Undefined Variable Error', 'Undefined Label Error', 'Illegal Flag Error', 'Illegal Immediate Error', 'Misuse Error', 'Var In Mid Error',
          'Missing Hlt Error', 'Hlt In Mid Error', 'Syntax Error', 'General Syntax Error']  # 10
reg = ['R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6']
var = {}
labels = {}
used= {}
instruction_number = [0]
