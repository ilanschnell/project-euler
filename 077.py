import itertools
from functools import lru_cache
from sympy.ntheory import primerange

# this is basically the same as problem 31

coins = list(primerange(1, 100))
Ncoins = len(coins)

@lru_cache(1024)
def count(amount, maxcoin=0):
    res = 0
    for i in range(maxcoin, Ncoins):
        amount_left = amount - coins[i]
        if amount_left == 0:
            res += 1
        if amount_left > 0:
            res += count(amount_left, i)
    return res

for n in itertools.count(2):
    if count(n) > 5000:
        print(n)
        break
