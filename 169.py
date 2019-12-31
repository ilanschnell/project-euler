from functools import lru_cache

@lru_cache
def count(n, exponent, repeats):
    if exponent < 0:
        return 1 if n == 0 else 0

    res = count(n, exponent - 1, 2)
    power = 1 << exponent
    upper = power * (repeats + 2)
    if repeats > 0 and power <= n < upper:
        res += count(n - power, exponent, repeats - 1)
    return res

n = 10 ** 25
print(count(n, n.bit_length() - 1, 2))
