from time import time
from bitarray import bitarray
from sympy.ntheory import primerange
from numba import njit

from bitarray.utils import count_n

@njit
def ith_fib(i):
    hi1 = hi2 = 1.0
    ex = 0
    lo1 = lo2 = 1
    n = 2
    while n < i:
        n += 1
        lo1, lo2 = lo2, (lo1 + lo2) % 10**16
        hi1, hi2 = hi2, hi1 + hi2
        if hi2 > 10:
            ex += 1
            hi1 /= 10
            hi2 /= 10
    return lo2, hi2, ex

@njit
def fiblen(m, nmax):
    a, b, n = 1, 1, 2
    while n < nmax:
        a, b = b, (a + b) % m
        n += 1
        if b == 0:
            return n
    return 0


def euler399(n):
    print("generating Fibonacci sieve")
    limit = int(n * 1.31)
    sffs = bitarray(limit)
    sffs.setall(True)  # square free Fibonacci sieve
    for p in primerange(1, 1500000):
        l = p * fiblen(p, limit // p + 1)
        if l:
            sffs[l - 1::l] = False
    print("counting")
    t0 = time()
    i = count_n(sffs, n)
    print("time:", time() - t0)
    print(i)
    print('%i,%.1fe%i' % ith_fib(i))

euler399(200)
euler399(10**8)
