# NOT WORKING YET
def hsd(n):
    for c in str(n):
        if c >= '3':
            return False
    return True

def g(n):
    if n == 999:
        return 111_222_222_222_222 // n
    if n == 9999:
        return 11_112_222_222_222_222_222 // n
    k = 1
    while True:
        if hsd(k * n):
            return k
        k += 1

res = 0
for n in range(1, 100 + 1):
    k = g(n)
    print(n, n*k, k)
    assert hsd(n*k)
    res += k
print(res)
