SEQ = "UDDDUdddDDUDDddDdDddDDUDDdUUDd"
START = 10 ** 15
#SEQ = "DdDddUUdDD"
#START = 10 ** 6

def is_good(a, seq):
    print(a, seq)
    for c in seq:
        ar3 = a % 3
        if ar3 == 0:
            if c != 'D':
                return False
            a /= 3
        elif ar3 == 1:
            if c != 'U':
                return False
            a = (4*a+2) / 3
        elif ar3 == 2:
            if c != 'd':
                return False
            a = (2*a-1) / 3
        else:
            raise
    return True

cur = START
step = 1
for length in range(1, len(SEQ) + 1):
    partial = SEQ[:length]
    while not is_good(cur, partial):
        cur += step
    step *= 3
print(cur)
