from functools import lru_cache

coins = (200, 100, 50, 20, 10, 5, 2, 1)
Ncoins = len(coins)

@lru_cache
def count(amount, maxcoin=0):
    if maxcoin == Ncoins - 1:
        return 1
    res = 0
    for i in range(maxcoin, Ncoins):
        amount_left = amount - coins[i]
        if amount_left == 0:
            res += 1
        if amount_left > 0:
            res += count(amount_left, i)
    return res

print(count(200))
