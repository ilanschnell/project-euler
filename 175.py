p, q = 123456789, 987654321

s = []
while q:
    if q >= p:
        n = q // p
        q -= n * p
    else:
        n = (p - 1) // q
        p -= n * q
    s.insert(0, str(n))

print(",".join(s))
