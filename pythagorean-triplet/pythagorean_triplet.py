import math


def triplets_with_sum(sum_of_triplet):
    s = set([])
    for a in range(1, sum_of_triplet // 3):
        for b in range(a + 1, sum_of_triplet // 2):
            for c in range(max(sum_of_triplet // 3, b + 1), min(sum_of_triplet // 2, math.floor(math.sqrt(2) * b))):
                if a + b + c == sum_of_triplet and is_triplet([a, b, c]):
                    s.add((a, b, c))
    return s


def is_triplet(triplet):
    return triplet[0] ** 2 + triplet[1] ** 2 == triplet[2] ** 2
