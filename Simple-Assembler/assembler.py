import sys
import error_detection
import compiler


def main():
    # code = list(map(str.strip,sys.stdin.readlines()))
    try:
        # '/Users/aayushgakhar/Documents/GitHub/CO_M21_Assignment/automatedTesting/tests/assembly/errorGen'
        #             '/test1'
        path='/Users/aayushgakhar/Desktop/test4'
        code = list(map(str.strip,open(path).readlines()))
    except:
        try:
            code = list(map(str.strip,open('/CO/ass co/CO_M21_Assignment/automatedTesting/tests/assembly/errorGen/test1')))
        except:
            # shrishti apna path idher likh le
            pass
    print(code)
    if error_detection.check(code):
        print('error')
    else:
        compiler.compile(code)
    print(code)


main()
var = dict()
lab = dict()
