from bitarray.util import gen_primes, sum_indices

a = gen_primes(2_000_000)

print('{:,d}'.format(sum_indices(a)))
