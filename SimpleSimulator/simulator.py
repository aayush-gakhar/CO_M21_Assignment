import sys
import system


def main():
    code = list(map(str.strip,sys.stdin.readlines()))
    # try:
    #     # '/Users/aayushgakhar/Documents/GitHub/CO_M21_Assignment/automatedTesting/tests/assembly/errorGen'
    #     #             '/test1'
    #     # path = '/Users/aayushgakhar/Documents/GitHub/CO_M21_Assignment/automatedTesting/tests/assembly/hardBin/test2'
    #
    #     path = '/Users/aayushgakhar/Documents/GitHub/CO_M21_Assignment/automatedTesting/tests/bin/hard/test2'
    #     code = list(map(str.strip,open(path).readlines()))
    # except:
    #     try:
    #         path = '/Users/aayushgakhar/Documents/GitHub/CO_M21_Assignment/automatedTesting/tests/bin/simple/test1'
    #         code = list(map(str.strip, open(path).readlines()))
    #     except:
    #         path = '/Users/aayushgakhar/Documents/GitHub/CO_M21_Assignment/automatedTesting/tests/bin/simple/test1'
    #         code = list(map(str.strip, open(path).readlines()))

    system.run(code)

main()