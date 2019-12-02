from math import log

values = []

for line in open('base_exp.txt'):
    b, e = [int(x) for x in line.strip().split(',')]
    values.append(e * log(b))

m  = max(values)
print(values.index(m) + 1)
