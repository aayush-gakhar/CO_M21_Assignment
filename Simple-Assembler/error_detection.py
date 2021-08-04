import sys


def check(code):
    typo(code)


def typo(code):
    for line in code:
        if not line:
            continue
        if line.split()[1] in Instructions:
            instruction_check()
        elif line.split()[1][-1] == ':':
            label_check()


def instruction_check():
    pass


def label_check():
    pass


def raise_error(error, line_no):
    error_flag = True
    sys.stdout.write(errors[error] + ' Line: ' + line_no)


Instructions = ['add', 'sub', 'mov', 'ld', 'st', 'mul', 'div', 'rs', 'ls', 'xor', 'or', 'and', 'not', 'cmp', 'jmp',
                'jlt', 'jgt', 'je', 'hlt']
error_flag = False
errors = ['NameError', 'VariableError', 'LabelError', 'FlagError', 'ImmediateError', 'MisuseError', 'VarInMidError',
          'MissingHltError', 'HltInMidError', 'SyntaxError', 'GeneralSyntaxError']
