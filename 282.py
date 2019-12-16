from sympy import totient, mod_inverse

# n = 0, 1, 2, 3
result = 1 + 3 + 7 + 61

p = 2 ** 8
q = 7 ** 8
modulo = p * q

phi_chain = [q]
k = q
while k > 1:
    k = totient(k)
    phi_chain.append(k)

# A(n, n) + 3 = 0 (mod 2^8)   for n > 3
u = p * mod_inverse(p, q)

# n = 4    A(4, 4) = 2^2^2^65536 - 3
w = 65536
for i in 2, 1, 0:
    w = pow(2, w, phi_chain[i])
result = (result + w * u - 3) % modulo

# n = 5, 6  A(5, 5) % modulo = A(6, 6) % modulo
w = 2
for phi in reversed(phi_chain):
    w = pow(2, w, phi)
result = (result + 2 * (w * u - 3)) % modulo

print(result)
