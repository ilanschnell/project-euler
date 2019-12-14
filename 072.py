# Very slow (90s), but short
from sympy.ntheory import totient

print(sum(totient(i) for i in range(2, 1000001)))
