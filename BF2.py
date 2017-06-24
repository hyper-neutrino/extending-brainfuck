'''

From BF1, adds numerical addition, subtraction, pointer movement, etc.

'''

import BF1

def blockify(code):
    blocks = []
    index = 0
    while index < len(code):
        string = ''
        if code[index] in '+-<>[],.':
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
            if index < len(blocks) - 1 and blocks[index + 1] not in '+-<>[],.':
                delta = int(blocks[index + 1])
                index += 1
            code += '+' * delta
        elif block == '-':
            delta = 1
            if index < len(blocks) - 1 and blocks[index + 1] not in '+-<>[],.':
                delta = int(blocks[index + 1])
                index += 1
            code += '-' * delta
        elif block == '<':
            delta = 1
            if index < len(blocks) - 1 and blocks[index + 1] not in '+-<>[],.':
                delta = int(blocks[index + 1])
                index += 1
            code += '<' * delta
        elif block == '>':
            delta = 1
            if index < len(blocks) - 1 and blocks[index + 1] not in '+-<>[],.':
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

def run(code, delay = 0, max = 0, min = 0):
    BF1.run(downgrade(code), delay = delay, max = max, min = min)
