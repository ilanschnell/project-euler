from fractions import Fraction


class Line(object):
    def __init__(self, ax, ay, bx, by):
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by
        if ax == bx:  # vertical line
            self.m = None
            self.t = Fraction(ax)
        else:
            self.m = Fraction(ay - by, ax - bx)
            self.t = ay - self.m * ax

    def __str__(self):
        return '(%s,%s) to (%s,%s)' % (self.ax, self.ay, self.bx, self.by)

def between(a, b, x):
    return min(a, b) < x < max(a, b)

def intercept(l1, l2):
    if l1.m is not None:  # l1 not vertical
        if l2.m is not None:  # l2 not vertical (normal case)
            if l1.m != l2.m:  # not parallel
                # x-coord of crossing point:
                x = (l2.t - l1.t) / (l1.m - l2.m)
                if between(l1.ax, l1.bx, x) and between(l2.ax, l2.bx, x):
                    return x, l1.m * x + l1.t

        else:  # l2 vertical
            if between(l1.ax, l1.bx, l2.t):
                # y-coord of crossing point:
                y = l1.m * l2.t + l1.t
                if between(l2.ay, l2.by, y):
                    return l2.t, y

    else:  # l1 vertical
        if l2.m is not None:  # l2 not vertical (only l1 vertical)
            return intercept(l2, l1)

    return None

def bbs(s=290797):
    while True:
        s = pow(s, 2, 50515093)
        yield s % 500

N = 5000
t = bbs()
lines = [Line(next(t), next(t), next(t), next(t)) for i in range(N)]

print(lines[0])
print(len(lines))

s = set()
for i in range(N):
    for j in range(i + 1, N):
        cp = intercept(lines[i], lines[j])
        if cp is None:
            continue
        s.add('%s,%s' % cp)
    print(i, len(s))

print(len(s))
