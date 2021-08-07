import sys
import system


def main():
    # code = sys.stdin.readlines()
    # print(code)
    try:
        # '/Users/aayushgakhar/Documents/GitHub/CO_M21_Assignment/automatedTesting/tests/assembly/errorGen'
        #             '/test1'
        # path = '/Users/aayushgakhar/Documents/GitHub/CO_M21_Assignment/automatedTesting/tests/assembly/hardBin/test2'

        path = '/Users/aayushgakhar/Documents/GitHub/CO_M21_Assignment/automatedTesting/tests/bin/simple/test1'
        code = list(map(str.strip,open(path).readlines()))
    except:
        try:
            path = '/Users/aayushgakhar/Documents/GitHub/CO_M21_Assignment/automatedTesting/tests/bin/simple/test1'
            code = list(map(str.strip, open(path).readlines()))
        except:
            path = '/Users/aayushgakhar/Documents/GitHub/CO_M21_Assignment/automatedTesting/tests/bin/simple/test1'
            code = list(map(str.strip, open(path).readlines()))

    # has_error, var, labels, instruction_number = error_detection.check(code)
    # # print(labels)
    # if not has_error:
    #     compiler.compile_(code,instruction_number,labels,var)

main()