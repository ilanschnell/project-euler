from bitarray.util import count_n, gen_primes


a = gen_primes(150_000)

m = 10_001
print(count_n(a, m) - 1)

# or using sympy
from sympy.ntheory import prime

print(prime(m))
