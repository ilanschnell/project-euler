from math import sqrt, ceil
from bitarray import bitarray


N = 100_000_000

isprime = bitarray(N + 2)
isprime.setall(True)
isprime[:2] = False
for i in range(2, ceil(sqrt(N))):
    if isprime[i]:
        isprime[i*i::i] = False

def valid(n):
    if not isprime[n + 1]:
        return False
    if not isprime[2 + n // 2]:
        return False
    for d in range(3, ceil(sqrt(n))):
        if n % d:
            continue
        if not isprime[d + n//d]:
            return False
    return True

res = 1
for n in range(2, N + 1, 4):
    if valid(n):
        res += n
print(res)
