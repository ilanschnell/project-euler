from decimal import getcontext, Decimal

precision = 5000
getcontext().prec = precision

def recur(d):
    f = str(Decimal(1) / Decimal(d))
    if len(f) <= precision:
        return 0
    f = f.strip('0.')
    for s in range(10):
        for r in range(1, 1000):
            if f[s:s+r] == f[s+r:s+2*r] == f[s+2*r:s+3*r] == f[s+3*r:s+4*r]:
                #print(d, s, r, f[:s], f[s:s+r])
                return r

assert recur(7) == 6

mr = 0
md = 0
for d in range(2, 1000):
    r = recur(d)
    if r > mr:
        mr = r
        md = d

print(md)
