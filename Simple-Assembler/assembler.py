import sys
import error_detection
import compiler


def main():
    # code = sys.stdin.readlines()
    try:
        code = open('/Users/aayushgakhar/Documents/GitHub/CO_M21_Assignment/automatedTesting/tests/assembly/errorGen'
                    '/test4')
    except:
        try:
            code = open('/CO/ass co/CO_M21_Assignment/automatedTesting/tests/assembly/errorGen/test1')
        except:
            # shrishti apna path idher likh le
            pass
    # print(list(code))
    if error_detection.check(code):
        print('error')
    else:
        compiler.compile(code)


main()
var = dict()
lab = dict()
