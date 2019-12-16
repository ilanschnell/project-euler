from itertools import permutations, product


def check(lst):
    targets = set()

    template = ['(xxx)x(xxx)',
                '((xxx)xx)xx',
                '(xx(xxx))xx',
                'xx((xxx)xx)',
                'xx(xx(xxx))']

    for x in permutations(lst):
        for o1, o2, o3, o4 in product('+-*/', repeat=4):
            for temp in template:
                temp = temp.replace('x', '%s')
                equation = temp % (x[0], o1, x[1], o2, x[2], o3, x[3])
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

m = 0
for d in range(1, 10):
    for c in range(1, d):
        for b in range(1, c):
            for a in range(1, b):
                n = check([a, b, c, d])
                if n >= m:
                    m = n
                    print(('%d%d%d%d %d') % (a, b, c, d, n))
