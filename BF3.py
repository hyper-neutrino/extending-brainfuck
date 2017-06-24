'''

From BF3: adds neighbor-wise operations

'''

import BF2, BFcore

def blockify(code):
    blocks = []
    index = 0
    while index < len(code):
        string = ''
        if code[index] not in '0123456789!?':
            blocks.append(code[index])
        elif code[index] in '!?':
            blocks.append(code[index] + code[index + 1])
            index += 1
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
        if block[0] == '!':
            if block[1] == '+':
                code += '>[<+>-]<'
            elif block[1] == '-':
                code += '>[<->-]<'
            elif block[1] == '*':
                code += '>>[-]<<<[>>+<<-]>[>[<<+>>>+<-]>[<+>-]<<-]>[-]<<'
            elif block[1] == '!':
                code += '[-]'
            elif block[1] == '>':
                code += '>[-]<[>+<-]>'
            elif block[1] == '<':
                code += '<[-]>[<+>-]<'
            elif block[1] == '@':
                code += '>>[-]<<[>>+<<-]>[<+>-]>[<+>-]<'
            elif block[1] == ',':
                code += ',[>,]'
        elif block[0] == '?':
            if block[1] == '+':
                code += '[>+<-]>'
            elif block[1] == '-':
                code += '[>-<-]>'
            elif block[1] == '*':
                code += '>>[-]>[-]<<[>+<-]<[>>[<+>>+<-]>[<+>-]<<<-]>>[-]<'
            elif block[1] == '?':
                code += '>[-]<'
            elif block[1] == '>':
                code += '>[-]>[-]<<[>+>+<<-]>>[<<+>>-]<'
            elif block[1] == '<':
                code += '<[-]<[-]>>[<+<+>>-]<<[>>+<<-]>'
            elif block[1] == '@':
                code += '<<[-]>>[<<+>>-]<[>+<-]<[>+<-]>'
            elif block[1] == ',':
                code += ',[<,]'
        else:
            code += block
        index += 1
    return code

def downgrade(code):
    return downgradeBlocks(blockify(code))

def run(code, delay = 0, max = 0, min = 0, debug = False):
    (BF2.debug if debug else BF2.run)(downgrade(BFcore.preprocess(code)), delay = delay, max = max, min = min)

def debug(code, delay = 0, max = 0, min = 0):
    print(__file__[__file__.rfind('/') + 1:-3], code)
    run(code, delay = delay, max = 0, min = 0, debug = True)
