from math import ceil, sqrt
from bitarray import bitarray

LIMIT = 10_000_000

sieve = []
for i in range(4):
    a = bitarray(LIMIT + 1)
    a.setall(0)
    sieve.append(a)

sn = ceil(sqrt(LIMIT))
for a in range(1, sn):
    b = 0
    while a * a + b * b <= LIMIT:
        b += 1
        for i, k in enumerate([1, 2, 3, 7]):
            n = a * a + k * b * b
            if n > LIMIT:
                break
            sieve[i][n] = 1

a = sieve[0]
for i in range(1, 4):
    a &= sieve[i]

print(a.count())
