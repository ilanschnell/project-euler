from bitarray import bitarray
from bitarray.util import count_n

N = 150_000

a = bitarray(N + 1)
a.setall(True)
a[:2] = False
for i in range(2, int(N ** 0.5) + 1):
    if a[i]:
        a[i*i::i] = False

m = 10_001
print(count_n(a, m) - 1)

# or using sympy
from sympy.ntheory import prime

print(prime(m))
