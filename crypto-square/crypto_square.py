from string import punctuation
import math


def encode(plain_text):
    normalized_text = ''.join(filter(str.isalnum, plain_text.lower()))
    l = len(normalized_text)
    c = math.ceil(math.sqrt(l))
    r = c - 1
    if r * c < l:
        r += 1
    s = ''
    for i in range(c):
        for j in range(r):
            if j * c + i < l:
                s += normalized_text[j * c + i]
            else:
                s += ' '
        if i < c - 1: s += ' '
    return s
