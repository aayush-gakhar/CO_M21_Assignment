import sys
import error_detection
import compiler


def main():
    code = [i.split() for i in sys.stdin.readlines()]

    # try:
    #     # '/Users/aayushgakhar/Documents/GitHub/CO_M21_Assignment/automatedTesting/tests/assembly/errorGen'
    #     #             '/test1'
    #     # path='/Users/aayushgakhar/Documents/GitHub/CO_M21_Assignment/automatedTesting/tests/assembly/hardBin/test2'
    #
    #     path = '/Users/aayushgakhar/Desktop/test'
    #     code = [i.split() for i in open(path).readlines()]
    # except:
    #     try:
    #         code = [i.split() for i in
    #                 open('/CO/ass co/CO_M21_Assignment/automatedTesting/tests/assembly/errorGen/test1').readlines()]
    #     except:
    #         path = 'C:/Users/hp/Documents/GitHub/assignment 1/automatedTesting/tests/assembly/errorGen/test3'
    #         code = [i.split() for i in open(path).readlines()]

    has_error, var, labels, instruction_number = error_detection.check(code)
    if has_error:
        print('error')
    else:
        compiler.compile_(code, instruction_number, labels, var)


main()
