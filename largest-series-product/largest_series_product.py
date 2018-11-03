def process(s):
    r = 1
    for i in s:
        r *= i
    return r


def largest_product(series, size):
    if size == 0:
        return 1
    if size > len(series) or size < 0:
        raise ValueError("Illegal case")
    l = list(map(int, series))
    series = [l[i: i + size] for i in range(len(series) - size + 1)]
    products = [process(s) for s in series]
    return max(products)
