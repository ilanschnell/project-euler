from itertools import count
from math import gcd


def A(n):
    for k in count(1):
        if pow(10, k, 9 * n) == 1:
            return k

assert A(7) == 6 and A(41) == 5

for n in count(1000000):
    if gcd(n, 10) != 1:
        continue
    a = A(n)
    print('A(%s) = %s' % (n, a))
    if a > 1000000:
        break
