from math import floor


def f(x):
    return floor(pow(2, 30.403243784 - x*x)) * 1e-9

u = -1.0
next = f(u)
for i in range(1, 513):
    u = next
    next = f(u)

print('%.9f' % (u + next))
