'''

Generic BF.

'''

import sys, time, BFcore, re

def carefulprint(code, end = ''):
    try:
        print(chr(code), end = '')
    except:
        pass

def interpret(code, delay = 0, max = 0, min = 0):
    code = re.sub('[^\\[\\]<>+-.,]', '', code)
    code = code.replace('[-]', '0').replace('[+]', '0')
    tape = [min]
    pointer = 0
    index = 0
    output = []
    while index < len(code):
        try:
            char = code[index]
            if char == '+':
                tape[pointer] += 1
                if max and tape[pointer] == max:
                    tape[pointer] = min
            elif char == '-':
                tape[pointer] -= 1
                if min and tape[pointer] == min:
                    tape[pointer] = max
            elif char == '<':
                pointer -= 1
                while pointer < 0:
                    pointer += 1
                    tape = [0] + tape
            elif char == '>':
                pointer += 1
                while pointer >= len(tape):
                    tape = tape + [0]
            elif char == '[':
                if not tape[pointer]:
                    brackets = 1
                    while brackets:
                        index += 1
                        if code[index] == '[':
                            brackets += 1
                        elif code[index] == ']':
                            brackets -= 1
            elif char == ']':
                if tape[pointer]:
                    brackets = -1
                    while brackets:
                        index -= 1
                        if code[index] == '[':
                            brackets += 1
                        elif code[index] == ']':
                            brackets -= 1
            elif char == ',':
                tape[pointer] = ord(sys.stdin.read(1))
            elif char == '.':
                output += [tape[pointer]]
            elif char == '0':
                tape[pointer] = 0
            index += 1
            for i in range(delay):
                time.sleep(1)
        except KeyboardInterrupt:
            print(str(tape))
            for codepoint in output:
                carefulprint(codepoint)
            print('')
    print('[%s]' % ', '.join('$%d$' % tape[i] if i == pointer else str(tape[i]) for i in range(len(tape))))
    for codepoint in output:
        carefulprint(codepoint)
    print('')

def run(code, delay = 0, max = 0, min = 0, debug = False):
    interpret((code), delay = delay, max = max, min = min)

def debug(code, delay = 0, max = 0, min = 0):
    print(__file__[__file__.rfind('/') + 1:-3], code)
    run(code, delay = delay, max = 0, min = 0, debug = True)
