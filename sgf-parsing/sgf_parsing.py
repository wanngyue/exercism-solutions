class SgfTree(object):
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for k, v in self.properties.items():
            if k not in other.properties:
                return False
            if other.properties[k] != v:
                return False
        for k in other.properties.keys():
            if k not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for a, b in zip(self.children, other.children):
            if a != b:
                return False
        return True


def parse(input):
    if len(input) == 0 or input.count(';') <= 0 or input.count('(') <= 0:
        raise ValueError('Input not right')
    i = 1
    fkey = 0
    key = ''
    fvalue = 0
    value = ''
    depth = 0
    children = []
    while i < len(input):
        if input[i] == '(':
            i += 1
            continue
        if input[i] == ';':
            depth += 1
            if depth == 1:
                dict = {}
                i += 1
                continue
            else:
                c_dict = {}
                key = ''
                i += 1
                continue
        if input[i] == '[':
            fvalue = 1
            i += 1
            continue
        if input[i] == ']':
            value = ''
            i += 1
            continue
        if input[i] == ')':
            key = ''
            if depth == 1:
                if input[i - 1] == ';':
                    break
                if fvalue == 1:
                    raise ValueError('Error')
                break
            else:
                children.append(SgfTree(c_dict))
                depth -= 1
                i += 1
                continue
        while input[i].isalpha() or input[i] == '\t' or input[i] == '\n' or input[i] == '\\' or input[i] == ' ':
            if input[i - 1] == ';' or fkey == 1:
                fkey = 1
                if input[i].islower():
                    raise ValueError("Key must be uppercase")
                key += input[i]
            elif fvalue == 1:
                if input[i] == '\t':
                    value += ' '
                elif input[i] == '\\':
                    i += 1
                    value += input[i]
                else:
                    value += input[i]

            i += 1
        if fkey == 1:
            if depth == 1:
                dict[key] = []
            else:
                c_dict[key] = []
            fkey = 0
            fvalue = 1
        elif fvalue == 1:
            if depth == 1:
                dict[key].append(value)
            else:
                c_dict[key].append(value)
            fvalue = 0

    return SgfTree(dict, children)
