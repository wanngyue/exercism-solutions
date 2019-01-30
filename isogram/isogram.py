def is_isogram(string):
    lowerstr = string.lower()
    return all(lowerstr.count(c) == 1 for c in lowerstr if c.isalpha())
