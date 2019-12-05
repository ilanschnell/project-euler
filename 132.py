"""
R(k) = (10^k  1) / 9

for a prime factor p:

-> R(k) = 0       (mod p)
-> 10^k - 1 = 0   (mod 9 * p)
-> 10^k = 1       (mod 9 * p)    where k = 10^9
"""
from sympy.ntheory import primerange

k = 1_000_000_000
s = n = 0
for p in primerange(1, 1000_000):
    if pow(10, k, 9 * p) == 1:
        n += 1
        s += p
        print(n, p)
        if n == 40:
            break
print(s)
