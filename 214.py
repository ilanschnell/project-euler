# very slow about 20 minutes
from sympy.ntheory import totient, primerange

CHAIN_LEN = 25
PRIME_LIMIT = 40_000_000

cache = {}

def chain(n):
    n = totient(n)
    m = n
    c = 0
    while n > 1:
        if n in cache:
            c += cache[n]
            n = 1
        else:
            c += 1
            n = totient(n)
        if c + 2 > CHAIN_LEN:
            return False
    cache[m] = c
    return c + 2 == CHAIN_LEN

s = 0
for p in primerange(1, PRIME_LIMIT):
    if chain(p):
        s += p
print(len(cache))
print(s)
