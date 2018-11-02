from __future__ import division
import math


class Rational(object):
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

    def __eq__(self, other):
        maximum_common_divisor = math.gcd(self.numer, self.denom)
        new_numer1 = self.numer // maximum_common_divisor
        new_denom1 = self.denom // maximum_common_divisor
        if new_numer1 * new_denom1 < 0:
            new_numer1 = -abs(new_numer1)
            new_denom1 = abs(new_denom1)

        maximum_common_divisor = math.gcd(other.numer, other.denom)
        new_numer2 = other.numer // maximum_common_divisor
        new_denom2 = other.denom // maximum_common_divisor
        if new_numer2 * new_denom2 < 0:
            new_numer2 = -abs(new_numer2)
            new_denom2 = abs(new_denom2)
        return (new_numer1 == new_numer2 == 0) or (new_numer1 == new_numer2 and new_denom1 == new_denom2)

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        new_numer = self.numer * other.denom + other.numer * self.denom
        new_denom = self.denom * other.denom
        maximum_common_divisor = math.gcd(new_numer, new_denom)
        new_numer = new_numer // maximum_common_divisor
        new_denom = new_denom // maximum_common_divisor
        return Rational(new_numer, new_denom)

    def __sub__(self, other):
        new_numer = self.numer * other.denom - other.numer * self.denom
        new_denom = self.denom * other.denom
        maximum_common_divisor = math.gcd(new_numer, new_denom)
        new_numer = new_numer // maximum_common_divisor
        new_denom = new_denom // maximum_common_divisor
        return Rational(new_numer, new_denom)

    def __mul__(self, other):
        new_numer = self.numer * other.numer
        new_denom = self.denom * other.denom
        maximum_common_divisor = math.gcd(new_numer, new_denom)
        new_numer = new_numer // maximum_common_divisor
        new_denom = new_denom // maximum_common_divisor
        return Rational(new_numer, new_denom)

    # (a1 * b2) / (a2 * b1)
    def __truediv__(self, other):
        new_numer = self.numer * other.denom
        new_denom = self.denom * other.numer
        maximum_common_divisor = math.gcd(new_numer, new_denom)
        new_numer = new_numer // maximum_common_divisor
        new_denom = new_denom // maximum_common_divisor
        if new_denom < 0:
            new_numer = -new_numer
            new_denom = -new_denom
        return Rational(new_numer, new_denom)

    def __abs__(self):
        new_numer = abs(self.numer)
        new_denom = abs(self.denom)
        return Rational(new_numer, new_denom)

    def __pow__(self, power):
        if power >= 0:
            new_numer = self.numer ** power
            new_denom = self.denom ** power
        else:
            new_denom = self.numer ** abs(power)
            new_numer = self.denom ** abs(power)
        return Rational(new_numer, new_denom)

    def __rpow__(self, base):
        return (base ** self.numer) ** (1 / self.denom)

