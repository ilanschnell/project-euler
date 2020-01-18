from math import sqrt

limit = 1_000_000_000_000

rep = set([1])
for base in range(2, int(sqrt(limit))):
    powers = base * base
    curr = 1 + base + powers
    while curr < limit:
        rep.add(curr)
        powers *= base
        curr += powers

print(sum(rep))
