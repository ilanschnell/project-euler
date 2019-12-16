from math import isclose
from itertools import permutations, product, count

templates = [t.replace('x', '%d').replace('o', '%s') for t in [
    '(x o x) o (x o x)',
    '((x o x) o x) o x',
    '(x o (x o x)) o x',
    'x o ((x o x) o x)',
    'x o (x o (x o x))',
]]

def check(lst):
    targets = set()

    for x1, x2, x3, x4 in permutations(lst):
        for o1, o2, o3 in product('+-*/', repeat=3):
            for temp in templates:
                equation = temp % (x1, o1, x2, o2, x3, o3, x4)
                try:
                    x = eval(equation)
                    i = int(round(x))
                    if isclose(i, x):
                        targets.add(i)
                except ZeroDivisionError:
                    pass

    for n in count(1):
        if n not in targets:
            return n - 1
    return 0

best = 0
for d in range(4, 10):
    for c in range(3, d):
        for b in range(2, c):
            for a in range(1, b):
                n = check([a, b, c, d])
                if n > best:
                    best = n
                    print(('%d%d%d%d %d') % (a, b, c, d, n))
