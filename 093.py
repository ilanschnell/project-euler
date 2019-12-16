from itertools import permutations, product

templates = [
    '(%d %s %d) %s (%d %s %d)',
    '((%d %s %d) %s %d) %s %d',
    '(%d %s (%d %s %d)) %s %d',
    '%d %s ((%d %s %d) %s %d)',
    '%d %s (%d %s (%d %s %d))',
]

def check(lst):
    targets = set()

    for x1, x2, x3, x4 in permutations(lst):
        for o1, o2, o3 in product('+-*/', repeat=3):
            for temp in templates:
                equation = temp % (x1, o1, x2, o2, x3, o3, x4)
                try:
                    f = eval(equation)
                    if f > 0.5:
                        i = int(f + 1E-8)
                        if abs(f - i) < 1E-8:
                            targets.add(i)
                except ZeroDivisionError:
                    pass

    for n in range(1, len(targets)):
        if n not in targets:
            return n - 1

best = 0
for d in range(4, 10):
    for c in range(3, d):
        for b in range(2, c):
            for a in range(1, b):
                n = check([a, b, c, d])
                if n > best:
                    best = n
                    print(('%d%d%d%d %d') % (a, b, c, d, n))
