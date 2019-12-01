def is_divisor(m):
    t1 = t2 = t3 = 1
    while True:
        t4 = t1 + t2 + t3
        t4 %= m
        if t4 == 0:
            return True
        t1 = t2
        t2 = t3
        t3 = t4
        if t1 == t2 == t3 == 1:
            return False

n = m = 1
while True:
    m += 2
    if not is_divisor(m):
        if n == 124:
            print(m)
            break
        n += 1
