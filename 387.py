# WORK IN PROGRESS
from sympy.ntheory import primerange, isprime

def digit_sum(n):
    return sum(int(d) for d in str(n))

def is_harshad(n):
    return n % digit_sum(n) == 0

def is_rt_harshad(n):
    s = str(n)
    for i in range(1, len(s) + 1):
        if not is_harshad(int(s[:i])):
            return False
    return True

def is_strong_harshad(n):
    i, j = divmod(n, digit_sum(n))
    if j:
        return False
    return isprime(i)

def count(N):
    res = 0
    for p in primerange(10, N):
        n = int(str(p)[:-1])
        if is_strong_harshad(n) and is_rt_harshad(n):
            res += p
    return res

assert count(10_000) == 90619
