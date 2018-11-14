def is_armstrong(number):
    return sum([int(c)**len(str(number)) for c in str(number)])==number
