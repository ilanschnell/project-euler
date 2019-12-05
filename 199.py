from math import sqrt

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

depth = 10
outer_k = 3 - 2 * sqrt(3)
outer_r = -1 / outer_k
inner_k = 1
inner_r = 1 / inner_k
initial = 3 * area(1)
v_shape = evaluate(outer_k, inner_k, inner_k, depth)
middle = evaluate(inner_k, inner_k, inner_k, depth)

result = (3 * area(inner_r) + 3 * v_shape + middle) / area(outer_r)
print("%.8f" % (1 - result))
