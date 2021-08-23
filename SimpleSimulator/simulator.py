import sys
import system


def main():
    code = list(map(str.strip, sys.stdin.readlines()))

    # try:
    #     # path = '/Users/aayushgakhar/Desktop/test 2'
    #
    #     path = '/Users/aayushgakhar/Documents/GitHub/CO_M21_Assignment/automatedTesting/tests/bin/hard/test2'
    #     code = list(map(str.strip, open(path).readlines()))
    # except:
    #     try:
    #         path = '/Users/aayushgakhar/Documents/GitHub/CO_M21_Assignment/automatedTesting/tests/bin/simple/test1'
    #         code = list(map(str.strip, open(path).readlines()))
    #     except:
    #         path = '/Users/aayushgakhar/Documents/GitHub/CO_M21_Assignment/automatedTesting/tests/bin/simple/test1'
    #         code = list(map(str.strip, open(path).readlines()))

    run(code,True)


def run(code, scatter=False):
    mem = system.MEM(code)
    pc = system.PC(0)
    rf = system.RF()
    ee = system.EE(mem, pc, rf)
    halted = False
    while not halted:
        Instruction = mem.load(pc)
        halted, new_pc = ee.execute(Instruction)
        pc.dump()
        rf.dump()
        pc.update(new_pc)
    mem.dump()
    if scatter:
        mem.show_traces()


main()
