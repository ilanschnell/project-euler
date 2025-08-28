from math import modf, sqrt


def is_square(x):
    return modf(sqrt(x))[0] == 0.0

def prop(x, y):
    return is_square(x + y) and is_square(x - y)

pa = {}

M = 1000
for stp in range(2, M, 2):
    for sxmy in range(1, M):
        sxpy = sxmy + stp
        if sxpy < M:
            xmy = sxmy * sxmy
            xpy = sxpy * sxpy
            x = (xmy + xpy) // 2
            y = x - xmy
            if x in pa:
                pa[x].append(y)
            else:
                pa[x] = [y]

sk = sorted(pa)
for x in sk:
    pa[x] = pa[x][::-1]

for x in sk:
    ys = pa[x]
    if len(ys) >= 2:
        for i, y in enumerate(ys[:-1]):
            for z in ys[i + 1:]:
                if prop(x, z) and prop(y, z):
                    print(x + y + z)
