from bisect import bisect_left
from math import log, prod
from sympy.ntheory import primerange

LIMIT = 190

primes = list(primerange(1, LIMIT))
log_primes = [log(x) for x in primes]
NP = len(primes)
print('NP', NP)
# I did not think about what happens in case the number of primes is odd
assert NP % 2 == 0
NH = NP // 2
p = prod(primes)
print('p', p)
hlogp = log(p) / 2
print('log(p)/2', hlogp)

NB = 1 << NH

lower = []
upper = []
for k in range(NB):
    lsum = usum = 0
    for i in range(NH):
        if (1 << i) & k:
            lsum += log_primes[i]
            usum += log_primes[i + NH]
    lower.append((lsum, k))
    upper.append((usum, k))

upper.sort()

d = []
for lsum, k in lower:
    i = bisect_left(upper, (hlogp - lsum, 0)) - 1
    d.append((lsum + upper[i][0], k + upper[i][1] * NB))

s, k = max(d)
print('       s', s)

res = prod(primes[i] for i in range(NP) if (1 << i) & k)
print('log(res)', log(res))
print(res)
print(res % (10 ** 16))
