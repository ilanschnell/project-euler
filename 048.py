modulo = 10_000_000_000

result = 0
for i in range(1, 1001):
    result += pow(i, i, modulo)
    result %= modulo
print(result)
