from math import sqrt

DEPTH = 10

def area(r):  # since everything is relative, we don't need pi here
    return r * r

def evaluate(k1, k2, k3, depth):
    k4 = k1 + k2 + k3 + 2 * sqrt(k1*k2 + k2*k3 + k1*k3)
    a = area(1 / k4)
    if depth == 1:
        return a
    return a + (evaluate(k1, k2, k4, depth - 1) +
                evaluate(k2, k3, k4, depth - 1) +
                evaluate(k1, k3, k4, depth - 1))

outer_k = 3 - 2 * sqrt(3)
outer_r = -1 / outer_k

inner_r = 1  # the 3 level 1 circles are defined to have radius 1
inner_k = 1 / inner_r

initial = 3 * area(inner_r)
v_shape = evaluate(outer_k, inner_k, inner_k, DEPTH)
middle = evaluate(inner_k, inner_k, inner_k, DEPTH)

result = (initial + 3 * v_shape + middle) / area(outer_r)
print("%.8f" % (1 - result))
