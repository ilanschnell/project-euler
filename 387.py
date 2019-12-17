from sympy.ntheory import isprime

def compute(N):
    result = 0

    # n must be a right-truncatable Harshad number, and the other
    # arguments are properties of the number n
    def find_harshad_primes(n, digitsum, is_strong):
        nonlocal result

        s = digitsum
        # shift left by 1 digit, and try all 10 possibilities
        # for the rightmost digit
        for m in range(10 * n, 10 * n + 10):
            if m >= N:
                break
            if is_strong and isprime(m):
                result += m
            j, r = divmod(m, s)
            if r == 0:
                find_harshad_primes(m, s, isprime(j))
            s += 1

    # All one-digit numbers are trivially Harshad numbers
    for i in range(1, 10):
        find_harshad_primes(i, i, False)

    return result

assert compute(10000) == 90619
print(compute(10**14))
