dict = {(0, 1, 2), (1, 2, 0), (2, 0, 1)}


def is_equilateral(sides):
    return all(sides) and len(set(sides)) == 1


def is_isosceles(sides):
    return is_equilateral(sides) or (len(set(sides)) == 2 and sum(sides) > 2 * max(sides))


def is_scalene(sides):
    return all(sides) and len(set(sides)) == 3 and sum(sides) > 2 * max(sides)
