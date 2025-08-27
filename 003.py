from bitarray.util import gen_primes


a = gen_primes(10_000)

n = 600851475143
while n > 1:
    for p in a.search(1):
        if n % p == 0:
            print(p)
            n //= p
            break
    else:
        raise ValueError("not enough primes")

assert n == 1
