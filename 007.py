from bitarray.util import ones, count_n

N = 150_000

a = ones(N + 1)
a[:2] = 0
for i in range(2, int(N ** 0.5) + 1):
    if a[i]:
        a[i*i::i] = 0

m = 10_001
print(count_n(a, m) - 1)

# or using sympy
from sympy.ntheory import prime

print(prime(m))
