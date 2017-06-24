'''

From BF4: adds functions

'''

import BF3, string, BFcore

def blockify(code):
    return code.split('\n')

def replace(names, functions, code):
    for index in range(min(len(names), len(functions))):
        code = code.replace(names[index], functions[index])
    return code

def downgrade(code):
    blocks = blockify(code)
    functions = blocks[:-1]
    names = string.ascii_lowercase + string.ascii_uppercase
    code = blocks[-1]
    ref = ''
    while ref != code:
        ref = code
        code = replace(names, functions, code)
    return code

def run(code, delay = 0, max = 0, min = 0, debug = False):
    (BF3.debug if debug else BF3.run)(downgrade(BFcore.preprocess(code)), delay = delay, max = max, min = min)

def debug(code, delay = 0, max = 0, min = 0):
    print(__file__[__file__.rfind('/') + 1:-3], code)
    run(code, delay = delay, max = 0, min = 0, debug = True)
