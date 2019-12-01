modulo = 100_000_000

def tetration(a, b):
    res = 1
    while b:
        res = pow(a, res, modulo)
        b -= 1
    return res

print(tetration(3, 2))
print(tetration(3, 3))
print(tetration(1777, 1855))
