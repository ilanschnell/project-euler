from functools import lru_cache

NUM_DIGITS = 18  # total number of digits
MAXUSE = 3       # maximum times each digitcan be used

@lru_cache(MAXUSE ** 10 * NUM_DIGITS)
def count(curr, length):
    if length == NUM_DIGITS:
        return 1

    result = 0

    for i in range(10):
        # cannot place 0 at first position
        if i == 0 and length == 0:
            continue
        # see if it is possible to use digit i
        if curr[i] < MAXUSE:
            next = list(curr)
            next[i] += 1
            result += count(tuple(next), length + 1)

    return result

print(count(tuple(10 * [0]), 0))
