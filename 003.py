from math import sqrt

from bitarray import bitarray


N = 1000_000
a = bitarray(N + 1)
a.setall(True)
a[:2] = False
for i in range(2, int(sqrt(N)) + 1):
    if a[i]:  # i is prime, so all multiples are not
        a[i*i::i] = False
primes = a.search(1)


n = 600851475143
while n > 1:
    for p in primes:
        if n % p == 0:
            print(p)
            n //= p
            break
