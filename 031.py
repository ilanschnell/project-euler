from functools import lru_cache

coins = (200, 100, 50, 20, 10, 5, 2, 1)
Ncoins = len(coins)

@lru_cache
def count(amount, maxcoin=0):
    if maxcoin == Ncoins - 1:
        return 1
    res = 0
    for i in range(maxcoin, Ncoins):
        if amount - coins[i] == 0:
            res += 1
        if amount - coins[i] > 0:
            res += count(amount - coins[i], i)
    return res

print(count(200))
