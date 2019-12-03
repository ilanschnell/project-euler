from math import gcd

limit = 10 ** 8

triples = []
for n in range(1, 5001):
    n2 = n * n
    for m in range(n + 1, 7251, 2):
        if gcd(n, m) != 1:
            continue
        m2 = m * m
        c = m2 + n2
        if c > limit // 2:
            continue
        a = m2 - n2
        b = 2 * m * n
        if a + b + c >= limit:
            continue
        if a > b:
            a, b = b, a
        if c % (b - a) == 0:
            assert gcd(a, b) == gcd(b, c) == gcd(a, c) == 1
            assert a < b < c
            assert b - a == 1
            print(a, b, c)
            triples.append((a, b, c))

count = 0

for a, b, c in triples:
    p = a + b + c
    s = limit // p
    print(p, s)
    count += s

print(count)
