from decimal import getcontext, Decimal

precision = 5000
getcontext().prec = precision

def recur(d):
    f = str(Decimal(1) / Decimal(d))
    if len(f) <= precision:
        return 0
    for r in range(1, 1000):
        if f[-2*r:-r] == f[-3*r:-2*r] == f[-4*r:-3*r]:
            #print(d, r, f[-2*r:-r])
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
