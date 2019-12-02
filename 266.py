import bisect
import operator
from math import log
from functools import reduce
from sympy.ntheory import primerange

def prod(iterable):
    return reduce(operator.mul, iterable, 1)

LIMIT = 190

primes = list(primerange(1, LIMIT))
log_primes = [log(x) for x in primes]
NP = len(primes)
print('NP', NP)
# I did not think about what happens in that the number of primes is odd
assert NP % 2 == 0
NH = NP // 2
p = prod(primes)
print('p', p)
log_p = log(p)
print('log(p)', log_p)
print('log(p)/2', log_p / 2)

NB = 2 ** NH

left = []
right = []
for k in range(0, NB):
    lsum = rsum = 0
    for i in range(0, NH):
        if (1 << i) & k:
            lsum += log_primes[i]
            rsum += log_primes[i + NH]
    left.append((lsum, k))
    right.append((rsum, k))

right.sort()

d = []
for lv, k in left:
    rv = log_p / 2 - lv
    m = bisect.bisect_left(right, (rv, 0)) - 1
    d.append((left[k][0] + right[m][0], k + right[m][1] * NB))

s, k = max(d)
print('       s', s)

res = prod(primes[i] for i in range(0, NP) if (1 << i) & k)
print('log(res)', log(res))
print(res)
print(res % (10 ** 16))
