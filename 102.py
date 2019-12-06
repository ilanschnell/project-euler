from math import acos, sqrt, pi


def prod2(a, b):
    return sum(a[i] * b[i] for i in range(2))

def gamma(a, b):
    return acos(prod2(a, b) / sqrt(prod2(a, a) * prod2(b, b)))

cnt = 0
for line in open('files/p102_triangles.txt'):
    data = [int(i) for i in line.split(',')]
    a = data[0:2]
    b = data[2:4]
    c = data[4:6]
    if gamma(a, b) + gamma(b, c) + gamma(c, a) > 2 * pi - 1e-10:
        cnt += 1
print(cnt)
