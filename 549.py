from sympy.ntheory import factorint


N = 100_000_000
cache = {}

def naive(n):
    m = 1
    res = 0
    while m % n != 0:
        res += 1
        m *= res
        m %= n
    return res

def sp(p, e):
    if e == 1:
        return p
    n = pow(p, e)
    if n in cache:
        return cache[n]
    m = 1
    res = 0
    while m % n != 0:
        res += p
        m *= res
        m %= n
    cache[n] = res
    return res

def s(n):
    return max(sp(p, e) for p, e in factorint(n).items())

r = 0
for n in range(2, N + 1):
    r += s(n)
    if n % 10_000 == 0:
        print(n, len(cache), r)
print(r)
