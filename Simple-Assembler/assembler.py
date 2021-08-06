import sys
import error_detection
import compiler


def main():
    code = [i.strip().split() for i in sys.stdin.readlines()]

    # try:
    #     # '/Users/aayushgakhar/Documents/GitHub/CO_M21_Assignment/automatedTesting/tests/assembly/errorGen'
    #     #             '/test1'
    #     path = '/Users/aayushgakhar/Documents/GitHub/CO_M21_Assignment/automatedTesting/tests/assembly/hardBin/test2'
    #
    #     # path = '/Users/aayushgakhar/Desktop/test4'
    #     #code = [i.strip().split() for i in open(path).readlines()]
    # except:
    #     try:
    #         code = [i.strip().split() for i in
    #                 open('/CO/ass co/CO_M21_Assignment/automatedTesting/tests/assembly/errorGen/test1').readlines()]
    #     except:
    #          path = ''  # srishti path
    #          code = [i.strip().split() for i in open(path).readlines()]
    #

    # print(code)
    has_error, var, labels, instruction_number = error_detection.check(code)
    # print(labels)
    if has_error:
        pass
        # print('error')
    else:
        compiler.compile_(code,instruction_number,labels,var)


main()
