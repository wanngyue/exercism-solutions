from string import ascii_lowercase as letters
def rotate(text, key):
    l=letters[key:]+letters[:key]
    trans= str.maketrans(letters+letters.upper(),l+l.upper())
    return text.translate(trans)
