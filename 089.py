roman_dict = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)

def roman2int(roman):
    w = [roman_dict[c] for c in roman]
    res = sum(w)
    for p in range(len(w) - 1):
        if w[p] < w[p + 1]:
            res -= 2 * w[p]
    return res

def int2roman(i):
    digits = [int(d) for d in '%04d' % i]
    res = [digits[0] * 'M']
    v = '.0.00.000.01.1.10.100.1000.02'.split('.')
    for n, t in (1, 'CDM'), (2, 'XLC'), (3, 'IVX'):
        res.extend(t[int(p)] for p in v[digits[n]])
    return ''.join(res)

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
