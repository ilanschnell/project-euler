from math import ceil, sqrt
from bitarray import bitarray

LIMIT = 10_000_000

sieve = bitarray(LIMIT + 1)
sieve.setall(1)

sn = ceil(sqrt(LIMIT))
for k in 1, 2, 3, 7:
    s = bitarray(LIMIT + 1)
    s.setall(0)
    for a in range(1, sn):
        a2 = a * a
        b = 0
        n = 0
        while n <= LIMIT:
            b += 1
            n = a2 + k * b * b
            if n > LIMIT:
                break
            s[n] = 1
    sieve &= s

print(sieve.count())
