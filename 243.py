from fractions import Fraction

from sympy.ntheory import totient, primerange

def R(d):
    return Fraction(totient(d), d-1)

TH = Fraction(15499, 94744)

d = 1
for p in primerange(1, 100):
    d *= p
    r = R(d)
    print(d, p, r)
    if r < TH:
        break
pp = d // p
print(pp)
for k in range(1, p):
    d = k * pp
    r = R(d)
    print(d, k, r)
    if r < TH:
        break
print(d)
