# very slow, takes 45 minutes
from math import isqrt
from bitarray import bitarray

LIMIT = 2_000_000_000

sieve = bitarray(LIMIT + 1)
sieve.setall(1)

sn = isqrt(LIMIT) + 1
for k in 1, 2, 3, 7:
    print('k =', k)
    s = bitarray(LIMIT + 1)
    for a in range(1, sn):
        a2 = a * a
        b = 0
        while 1:
            b += 1
            n = a2 + k * b * b
            if n > LIMIT:
                break
            s[n] = 1
    sieve &= s

print(sieve.count())
