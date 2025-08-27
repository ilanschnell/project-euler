from math import ceil, sqrt

from bitarray.util import gen_primes


N = 100_000_000

prime = gen_primes(N + 2)

def valid(n):
    if not prime[n + 1]:
        return False
    if not prime[2 + n // 2]:
        return False
    for d in range(3, ceil(sqrt(n))):
        if n % d:
            continue
        if not prime[d + n // d]:
            return False
    return True

res = 1
for n in range(2, N + 1, 4):
    if valid(n):
        res += n
print(res)
