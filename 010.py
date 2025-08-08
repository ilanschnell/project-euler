from math import isqrt

from bitarray.util import ones, sum_indices

N = 2_000_000

a = ones(N)    # each bit a[i] corresponds to whether or not i is a prime
a[:2] = False  # zero and one are not prime
for i in range(2, isqrt(N) + 1):  # perform sieve
    if a[i]:  # i is prime, so all multiples are not
        a[i*i::i] = False

print('{:,d}'.format(sum_indices(a)))
