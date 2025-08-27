from bitarray import bitarray

is_sqr = bitarray(1_000_000)
for i in range(1000):
    is_sqr[i * i] = 1

def prop(x, y):
    return is_sqr[x + y] and is_sqr[x - y]

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
