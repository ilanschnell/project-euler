from fractions import Fraction

a = Fraction(1, 2)
s = 0
for n in range(1000):
    b = 1 + a
    s += len(str(b.numerator)) > len(str(b.denominator))
    a = 1 / (2 + a)

print(s)
