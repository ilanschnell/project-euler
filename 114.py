from functools import cache

rml = 3  # red minimum length

@cache
def count(n):
    if n < rml:
        # only one way of doing this (using n grey cells)
        return 1

    return (
        # one option is to leave next cell grey
        count(n - 1) +
        # sum options with red (of length rml..n-1), then 1 grey
        sum(count(n - red - 1) for red in range(rml, n)) +
        # one way to have red block of len n
        1)

assert count(7) == 17
print(count(50))
