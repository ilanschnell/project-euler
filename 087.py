from math import sqrt
from bitarray import bitarray
from sympy.ntheory import primerange

LIMIT = 50_000_000

primes = list(primerange(1, sqrt(LIMIT)))

ba = bitarray(LIMIT)
ba.setall(0)

for a in primes:
    a2 = pow(a, 2)
    for b in primes:
        b3 = pow(b, 3)
        if b3 > LIMIT:
            break
        for c in primes:
            n = a2 + b3 + pow(c, 4)
            if n >= LIMIT:
                break
            ba[n] = 1

print(ba.count())
