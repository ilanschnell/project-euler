from math import log10
from numba import njit

@njit
def p(L, n):
    lg2 = log10(2.0)
    lgL = log10(L)
    lgL1 = log10(L + 1)
    j = 0
    cnt = 0
    while cnt < n:
        j += 1
        m = int(j * lg2 - lgL)
        if lgL < j * lg2 - m < lgL1:
            cnt += 1
    return j

print(p(12, 1))
print(p(12, 2))
print(p(123, 45))
print(p(123, 678910))
