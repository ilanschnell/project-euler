N = 10**17

fib = [1, 2]
fibosum = [1, 2, 3]
while fib[-1] < N:
    fib.append(fib[-1] + fib[-2])
    fibosum.append(fibosum[-1] + fibosum[-2] + fib[-2] - 1)

print(fib)
print(fibosum)
N -= 1

def zeckendorf(x):
    result = 0
    p = len(fib)
    while x > 0:
        p -= 2  # nonconsecutive!
        while fib[p] > x:
            p -= 1
        x -= fib[p]
        result += 1
    return result

def search(x):
    p = 0
    while fib[p + 1] <= x:
        p += 1
    reduced = x - fib[p]
    if reduced == 0:
        return fibosum[p]
    return fibosum[p] + reduced + search(reduced)

print(search(N))
