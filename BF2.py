'''

From BF2, adds numerical addition, subtraction, pointer movement, etc.

'''

import BF1, re, BFcore

def blockify(code):
    blocks = []
    index = 0
    while index < len(code):
        string = ''
        if code[index] not in '0123456789':
            blocks.append(code[index])
        while index < len(code) and code[index] in '0123456789':
            string += code[index]
            index += 1
        if string:
            blocks.append(string)
        else:
            index += 1
    return blocks

def downgradeBlocks(blocks):
    code = ''
    index = 0
    while index < len(blocks):
        block = blocks[index]
        if block == '+':
            delta = 1
            if index < len(blocks) - 1 and re.match('^\d+$', blocks[index + 1]):
                delta = int(blocks[index + 1])
                index += 1
            code += '+' * delta
        elif block == '-':
            delta = 1
            if index < len(blocks) - 1 and re.match('^\d+$', blocks[index + 1]):
                delta = int(blocks[index + 1])
                index += 1
            code += '-' * delta
        elif block == '<':
            delta = 1
            if index < len(blocks) - 1 and re.match('^\d+$', blocks[index + 1]):
                delta = int(blocks[index + 1])
                index += 1
            code += '<' * delta
        elif block == '>':
            delta = 1
            if index < len(blocks) - 1 and re.match('^\d+$', blocks[index + 1]):
                delta = int(blocks[index + 1])
                index += 1
            code += '>' * delta
        elif block in '[],.':
            code += block
        else:
            code += '+' * int(block)
        index += 1
    return code

def downgrade(code):
    return downgradeBlocks(blockify(code))

def run(code, delay = 0, max = 0, min = 0, debug = False):
    (BF1.debug if debug else BF1.run)(downgrade(BFcore.preprocess(code)), delay = delay, max = max, min = min)

def debug(code, delay = 0, max = 0, min = 0):
    print(__file__[__file__.rfind('/') + 1:-3], code)
    run(code, delay = delay, max = 0, min = 0, debug = True)
