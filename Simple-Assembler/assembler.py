import sys
import error_detection
import compiler


def main():
    # code = list(map(str.strip,sys.stdin.readlines()))
    try:
        # '/Users/aayushgakhar/Documents/GitHub/CO_M21_Assignment/automatedTesting/tests/assembly/errorGen'
        #             '/test1'
        # path='/Users/aayushgakhar/Documents/GitHub/CO_M21_Assignment/automatedTesting/tests/assembly/errorGen/test2'

        path='/Users/aayushgakhar/Desktop/test4'
        code = list(map(str.strip,open(path).readlines()))
    except:
        try:
            code = list(map(str.strip,open('/CO/ass co/CO_M21_Assignment/automatedTesting/tests/assembly/simpleBin/test5').readlines()))
        except:
            # shrishti apna path idher likh le
            pass
    print(code)
    has_error, var, labels=error_detection.check(code)
    if has_error:
        print('error')
    else:
        compiler.compile(code)


main()
var = dict()
lab = dict()
