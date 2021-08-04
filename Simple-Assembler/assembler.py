import sys
import error_detection


def main():
    code = sys.stdin.readlines()
    error_detection.check(code)

main()