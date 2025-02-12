from functools import cache

coins = [200, 100, 50, 20, 10, 5, 2, 1]
Ncoins = len(coins)

@cache
def count(amount, maxcoin=0):
    """
    Given some amount of money, and the index of the largest coin to use,
    return the number of combinations the amount can be made.
    """
    res = 0
    for i in range(maxcoin, Ncoins):
        amount_left = amount - coins[i]
        if amount_left == 0:
            res += 1
        if amount_left > 0:
            res += count(amount_left, i)
    return res

print(count(200))
