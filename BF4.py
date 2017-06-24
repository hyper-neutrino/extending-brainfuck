'''

From BF4: adds functions

'''

import BF3, BFcore, re

def blockify(code):
    return code.split('\n')

def replace(functions, code):
    for name in functions:
        code = code.replace(name, functions[name])
    return code

def downgrade(code):
    blocks = blockify(code)
    functions = {}
    code = ''
    for block in blocks:
        if re.match('^\w+:.+$', block):
            functions[block[:block.index(':')]] = block[block.index(':') + 1:]
        else:
            code += block + '\n'
    ref = ''
    while ref != code:
        ref = code
        code = replace(functions, code)
    return code

def run(code, delay = 0, max = 0, min = 0, debug = False):
    (BF3.debug if debug else BF3.run)(downgrade(BFcore.preprocess(code)), delay = delay, max = max, min = min)

def debug(code, delay = 0, max = 0, min = 0):
    print(__file__[__file__.rfind('/') + 1:-3], code)
    run(code, delay = delay, max = 0, min = 0, debug = True)
