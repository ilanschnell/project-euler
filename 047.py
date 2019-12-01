import itertools
from sympy.ntheory import factorint

N = 4

def valid(i):
    for j in range(N):
        if len(factorint(i + j)) != N:
            return False
    return True

for i in itertools.count():
    if valid(i):
        print(i)
        break
