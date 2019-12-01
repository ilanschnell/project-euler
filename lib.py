from math import factorial


def bico(n,r):
    if r > n:
        return 0
    return factorial(n) // factorial(r) // factorial(n - r)


class Memoize:
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args, **keywords):
        key = (args, tuple(keywords.items()))
        if key not in self.cache:
            self.cache[key] = self.func(*args, **keywords)
        return self.cache[key]
