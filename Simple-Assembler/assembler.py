import sys
import error_detection
import compiler


def main():
    # code = sys.stdin.readlines()
    code=open('/Users/aayushgakhar/Documents/GitHub/CO_M21_Assignment/automatedTesting/tests/assembly/errorGen/test1')
    print([i for i in code])
    if(error_detection.check(code)):
        return
    compiler.compile(code)


main()
var=dict()
lab=dict
