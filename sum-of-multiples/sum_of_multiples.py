def sum_of_multiples(limit, multiples):
    return sum(n for n in range(1, limit) if any(n % m == 0 for m in multiples))
