symbols = {'[': ']', '{': '}', '(': ')'}


def is_paired(input_string):
    stack = []
    for c in input_string:
        if c in symbols.keys():
            stack.append(c)
        elif c in symbols.values():
            if not stack or symbols[stack.pop()] != c:
                return False
    return not stack
