import re
def verify(isbn):
    s = isbn.replace('-', '').lower()
    if not re.compile("[0-9]{9}([0-9]|x)$").match(s):
        return False
    ds=list(s)
    if ds[-1]=='x':
        ds[-1]='10'
    return sum(factors[0]*factors[1] for factors in zip(map(int,ds),range(10,0,-1)))%11==0