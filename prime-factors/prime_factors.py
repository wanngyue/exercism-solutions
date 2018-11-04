def prime_factors(natural_number):
    primes = []
    tmp = 2
    while natural_number > 1:
        if natural_number % tmp == 0:
            primes.append(tmp)
            natural_number = natural_number // tmp
        else:
            tmp += 1
    return primes
