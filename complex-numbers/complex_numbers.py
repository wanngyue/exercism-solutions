import math


class ComplexNumber(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        return ComplexNumber(self.real * other.real - self.imaginary * other.imaginary,
                             self.imaginary * other.real + self.real * other.imaginary)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    # (a * c + b * d)/(c^2 + d^2) + (b * c - a * d)/(c^2 + d^2) * i

    def __truediv__(self, other):
        base = other.real ** 2 + other.imaginary ** 2
        return ComplexNumber((self.real * other.real + self.imaginary * other.imaginary) / base,
                             (self.imaginary * other.real - self.real * other.imaginary) / base)

    def __abs__(self):
        return math.sqrt(self.real ** 2 + self.imaginary ** 2)

    def conjugate(self):
        return ComplexNumber(self.real, -1 * self.imaginary)

    def exp(self):
        return ComplexNumber(math.exp(self.real), 0) * ComplexNumber(math.cos(self.imaginary), math.sin(self.imaginary))

    def __repr__(self):
        return f're:{self.real}, im:{self.imaginary}'