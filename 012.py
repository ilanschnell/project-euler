from math import prod
from sympy.ntheory import factorint

t = n = 1
while True:
    n += 1
    t = t + n
    # number of divisors
    d = prod(a + 1 for a in factorint(t).values())
    if d > 500:
        print(t)
        break
