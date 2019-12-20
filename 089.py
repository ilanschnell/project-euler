roman_dict = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)

def roman2int(R):
    w = [roman_dict[c] for c in R]
    res = sum(w)
    for p in range(len(w) - 1):
        if w[p] < w[p + 1]:
            res -= 2 * w[p]
    return res

def int2roman(i):
    n, i = divmod(i, 1000)
    res = n * 'M'
    for n in 2, 1, 0:
        w = '.0.00.000.01.1.10.100.1000.02'.split('.')[i // 10 ** n % 10]
        res += ''.join('IVXLCDM'[int(p) + 2 * n] for p in w)
    return res

chars_saved = 0
for line in open('files/p089_roman.txt'):
    old = line.strip()
    new = int2roman(roman2int(old))
    chars_saved += len(old) - len(new)

print('Characters saved:', chars_saved)

for n in range(1, 7170):
    assert roman2int(int2roman(n)) == n
for n in range(1, 7):
    print(int2roman(n))
