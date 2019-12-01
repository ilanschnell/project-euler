from sympy.ntheory import primerange, factorint

def M(p, q, N):
    res = 0
    for i in range(N+1, 1, -1):
        factors = factorint(i)
        if (len(factors) == 2 and p in factors and q in factors):
            res = i
            break
    return res

def S(N):
    s = 0
    for i in primerange(2, N ** 0.5 + 1):
        for j in primerange(i + 1, N // 2):
            prod = i * j
            if prod > N:
                break
            maxProd = 0
            while prod <= N:
                curr = prod
                while curr * j <= N:
                    curr *= j
                if maxProd < curr:
                    maxProd = curr
                prod *= i
            s += maxProd
    return s

print(M(2, 3, 100))
print(M(3, 5, 100))
print(M(2, 73, 100))
print(S(100)) # 2662
print(S(10_000)) # 16373230
print(S(1_000_000)) # 124397236942
print(S(10_000_000))
