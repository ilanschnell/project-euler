# VERY SLOW 20 MINUTES
from sympy.ntheory import isprime

N = 50_000_000

cnt = 0
for n in range(2, N + 1):
    t = 2 * n * n - 1
    if not isprime(t):
        continue
    cnt += 1
    if cnt % 1000 == 0:
        print(n, t, cnt)

print(cnt)
