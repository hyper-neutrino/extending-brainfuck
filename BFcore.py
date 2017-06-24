import re

def preprocess(code):
    return '\n'.join(re.sub('#.+$', '', line) for line in code.split('\n'))
