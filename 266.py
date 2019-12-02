import bisect
from math import log
from sympy.ntheory import primerange

LIMIT = 190

primes = list(primerange(1, LIMIT))
NP = len(primes)
print('NP', NP)
NH = NP // 2

p = 1
for i in primes:
    p *= i
print('p', p)
log_p = log(p)
print('log(p)', log_p)

log_primes = [log(x) for x in primes]

N = 2 ** NH

left = []
right = []
for k in range(0, N):
    ls = rs = 0
    for i in range(0, NH):
        if (1 << i) & k:
            ls += log_primes[i]
            rs += log_primes[i + NH]
    left.append((ls, k))
    right.append((rs, k))

right.sort()

d = []
for lv, k in left:
    rv = log_p / 2 - lv
    i, j = 0, N
    m = bisect.bisect_left(right, (rv, 0)) - 1
    s = left[k][0] + right[m][0]
    d.append((s, k, right[m][1]))

print(log_p / 2)
s, k, m = max(d)

x = k + m * N
res = 1
for i in range(0, NP):
    if (1 << i) & x:
        res *= primes[i]
print('log(res)', log(res))
print(res)
print(res % int(1E16))
