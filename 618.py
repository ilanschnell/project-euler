from array import array

from sympy.ntheory import primerange


n = 50000
MOD = 1000_000_000

f = array('i', n*[0])
f[0] = 1

for p in primerange(1, n):
    for i in range(p, n):
        f[i] = (f[i] + f[i - p] * p) % MOD
    print(p)

for k in range(20):
    print(k, f[k])

ans = 0
a = b = 1
for k in range(2, 25):
    c = a + b
    print('a=', a)
    ans = (ans + f[a]) % MOD
    b, a = a, c

print(ans)
