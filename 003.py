from math import ceil, sqrt

from bitarray import bitarray


N = 10_000
a = bitarray(N + 1)
a.setall(True)
a[:2] = False
for i in range(2, ceil(sqrt(N))):
    if a[i]:  # i is prime, so all multiples are not
        a[i*i::i] = False

n = 600851475143
while n > 1:
    for p in a.itersearch(1):
        if n % p == 0:
            print(p)
            n //= p
            break
    else:
        raise ValueError("not enough primes")

assert n == 1
