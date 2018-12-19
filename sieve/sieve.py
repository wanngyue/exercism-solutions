def sieve(limit):
    bits = [1] * (limit - 1)#assume all are prime
    for i in range(2, limit + 1):
        if bits[i - 2]:
            for j in range(i * 2, limit + 1, i):
                bits[j - 2] = 0#set this number as non prime

    return [i for i in range(2, limit + 1) if bits[i-2] == 1]
