S = '1_2_3_4_5_6_7_8_9_0'  # len 19

def isok(n):
    s = str(n)
    if len(s) != 19:
        return False
    for i in range(19):
        c = S[i]
        if c != '_' and s[i] != c:
            return False
    return True

n = 1010101010  # int(S.replace('_', '0')) ** .5
while not isok(n * n):
    n += 10  # because square has to end with 0

print(n)
