from sympy.ntheory import primerange, isprime

N = 1_000_000

primes = list(primerange(1, N))

ls = 0
for s in range(len(primes) - 2000):
    r = primes[s]
    for t in range(1, 2000):
        r += primes[s + t]
        if r > N:
            break
        if isprime(r):
            if t + 1 > ls:
                print(r, t + 1)
                ls = t + 1
