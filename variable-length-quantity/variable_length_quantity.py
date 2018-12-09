import math


def encode(numbers):
    l = []
    for number in numbers:
        n = math.ceil((len(bin(number)) - 2) / 7)
        mask = (1 << 7) - 1
        series = [number & mask]
        for i in range(1, n):
            var = (number >> i * 7) & mask
            var |= 1 << 7
            series.append(var)
        l.extend(reversed(series))
    return l


def decode(bytes_):
    if len(bytes_) == 1 and (bytes_[0] & (1 << 7)):
        raise ValueError('ERR')
    mask = (1 << 7) - 1
    res = []
    v = 0
    i = 0
    while i < len(bytes_):
        value = bytes_[i] & mask  # slice first 7 bits
        v = (v << 7) + value
        end = not (bytes_[i] & (1 << 7))  # check if 7th bit ==1
        if end:
            res.append(v)
            v = 0
        i += 1
    return res
