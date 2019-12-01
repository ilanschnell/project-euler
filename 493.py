import random

from sympy import binomial

N = 100_000

a = 10 * list(range(7))

n = 0
for _ in range(N):
    random.shuffle(a)
    n += len((set(a[:20])))

print(n / N)

print('%.9f' % (7 * (1 - binomial(60, 20) / binomial(70, 20))))
