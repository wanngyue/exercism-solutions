import math


def classify(number):
    if number <= 0:
        raise ValueError("Not a natural number")
    if number == 1:
        return 'deficient'
    l = [1]
    for i in range(2, number):
        if number % i == 0:
            l.append(i)
    s = 'perfect' if sum(l) == number else 'abundant' if sum(l) > number else 'deficient'
    return s
