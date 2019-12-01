from sympy import mod_inverse
from sympy.ntheory import primerange, isprime


def facmod(n, m):
    if n >= m:
        return 0
    res = m - 1
    for i in range(m - 1, n, -1):
        res *= mod_inverse(i, m)
        res %= m
    return res

def S(i):
    assert isprime(i)
    minus5 = facmod(i - 5, i)
    minus4 = (minus5 * (i - 4)) % i
    minus3 = (minus4 * (i - 3)) % i
    minus2 = (minus3 * (i - 2)) % i
    minus1 = i - 1 # Wilson's theorem
    return (minus1 + minus2 + minus3 + minus4 + minus5) % i

res = 0
for n, p in enumerate(primerange(5, 1E8)):
    res += S(p)
    if n % 1000 == 0:
        print(p, res)
print(res)
