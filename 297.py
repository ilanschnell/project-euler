# WIP
N = 1000_000

fib = [1, 2]
while fib[-1] < N:
    fib.append(fib[-1] + fib[-2])

def zeckendorf(x):
    result = 0
    p = len(fib) - 1
    while x > 0:
        while fib[p] > x:
            p -= 1
        x -= fib[p]
        result += 1
    return result

result = 0
for i in range(N):
    result += zeckendorf(i)
print(result)
