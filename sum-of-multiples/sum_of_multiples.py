def has_any_multiple(number, multiples):
    return any(number % m == 0 for m in multiples)

def sum_of_multiples(limit, multiples):
    return sum(n for n in range(1, limit) if has_any_multiple(n, multiples))
