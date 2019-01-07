l = [" _ | ||_|   ", "     |  |   ", " _  _||_    ", " _  _| _|   ",
     "   |_|  |   ", " _ |_  _|   ", " _ |_ |_|   ", " _   |  |   ",
     " _ |_||_|   ", " _ |_| _|   "]


def transfer(s):
    try:
        i = l.index(s)
    except ValueError:
        return '?'
    if 0 <= i <= 9:
        return str(i)
    else:
        return str('?')


def convert(g):
    if not g or len(g) % 4 or len(g[0]) % 3:
        raise ValueError('ERR')

    res = ""
    for row in range(0, len(g), 4):
        for col in range(0, len(g[0]), 3):
            res +=transfer(''.join(g[row+i][col:col + 3] for i in range(4)))
        res += ','

    return res.strip(',')
