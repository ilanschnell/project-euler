# very slow about 10 minutes
from sympy.ntheory import totient, primerange

CHAIN_LEN = 25
PRIME_LIMIT = 40_000_000

cache = {}

def chain(n):
    n -= 1  # if n is prime, then totient(n) = n - 1
    m = n
    s = 0
    while n > 1:
        if n in cache:
            s += cache[n]
            break
        n = totient(n)
        s += 1
    cache[m] = s
    return s + 2 == CHAIN_LEN

result = 0
for p in primerange(1, PRIME_LIMIT):
    if chain(p):
        result += p
print(len(cache))
print(result)
