from sympy import binomial, factorint

N = 51

def is_sqr_free(n):
    return not any(k > 1 for k in factorint(n).values())

s = {1}
for n in range(1, N):
    for k in range(1, n):
        s.add(binomial(n, k))

result = sum(n for n in s if is_sqr_free(n))
print(result)
