from math import isqrt
from bitarray import bitarray
from sympy.ntheory import primerange

LIMIT = 50_000_000

primes = list(primerange(1, isqrt(LIMIT) + 1))

mark = bitarray(LIMIT)

for a in primes:
    a2 = pow(a, 2)
    for b in primes:
        b3 = pow(b, 3)
        if b3 > LIMIT:
            break
        for c in primes:
            c4 = pow(c, 4)
            n = a2 + b3 + c4
            if n >= LIMIT:
                break
            mark[n] = 1

print(mark.count())
