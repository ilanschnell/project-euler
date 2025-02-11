from itertools import count
from functools import cache

@cache
def F(m, n): # see 114.py
    if n < m:
        return 1
    return (
        F(m, n - 1) +
        sum(F(m, n - r - 1) for r in range(m, n)) + 1)

assert F(3, 29) == 673135
assert F(3, 30) == 1089155
assert F(10, 56) == 880711
assert F(10, 57) == 1148904

for n in count(1):
    if F(50, n) > 1_000_000:
        break
print(n)
