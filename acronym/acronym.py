import re


def abbreviate(words):
    pattern = re.compile(r"\w+")
    ws = pattern.findall(words.replace('\'', ''))
    return ''.join(w[0].upper() for w in ws)
