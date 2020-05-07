####################################################################################################
# quaternion.py
# Ben Kallus
# 5/7/2020
#
# You are free to use this however you like. Feel free to credit me or not.
####################################################################################################

from fractions import Fraction

class Quaternion:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __mul__(self, other):
        a = (self.a * other.a) - (self.b * other.b) - (self.c * other.c) - (self.d * other.d)
        b = (self.a * other.b) + (self.b * other.a) + (self.c * other.d) - (self.d * other.c)
        c = (self.a * other.c) + (self.c * other.a) + (self.d * other.b) - (self.b * other.d)
        d = (self.a * other.d) + (self.d * other.a) + (self.b * other.c) - (self.c * other.b)

        return Quaternion(a, b, c, d)

    def __add__(self, other):
        return Quaternion(self.a + other.a, self.b + other.b, self.c + other.c, self.d + other.d)

    def __str__(self):
        result = ""
        if self.a != 0:
            result += str(self.a)
        if self.b != 0:
            if self.b == 1:
                result += "+i"
            elif self.b == -1:
                result += "-i"
            elif self.b != 0:
                result += ("+" if self.b >= 0 else "") + str(self.b) + "i"
        if self.c != 0:
            if self.c == 1:
                result += "+j"
            elif self.c == -1:
                result += "-j"
            elif self.c != 0:
                result += ("+" if self.c >= 0 else "") + str(self.c) + "j"
        if self.d != 0:
            if self.d == 1:
                result += "+k"
            elif self.d == -1:
                result += "-k"
            elif self.d != 0:
                result += ("+" if self.d >= 0 else "") + str(self.d) + "k"

        if result.startswith("+"):
            result = result[1:]

        return result

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b and self.c == other.c and self.d == other.d

    def __repr__(self):
        return str(self)

    def __hash__(self):
        return hash(repr(self))

    def conjugate(self):
        return Quaternion(self.a, -self.b, -self.c, -self.d)

    def _divide(self, x):
        return Quaternion(Fraction(self.a, x), Fraction(self.b, x), Fraction(self.c, x), Fraction(self.d, x))

    def inverse(self):
        return self.conjugate()._divide(self.a**2 + self.b**2 + self.c**2 + self.d**2)
