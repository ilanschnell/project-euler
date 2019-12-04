from collections import defaultdict
from itertools import product
from functools import lru_cache

WIDTH = 32
HEIGHT = 10

all_rows = []

def generate_rows(row):
    row = list(row)
    w = row[-1] if row else 0  # current width
    if w + 2 == WIDTH or w + 3 == WIDTH:  # just one brick left?
        all_rows.append(row)
        return
    if w + 1 == WIDTH:  # gap too small for a brick?
        return
    # add a small brick
    row.append(w + 2)
    generate_rows(row)
    # replace last 2-brick by 3-brick
    row[-1] += 1
    generate_rows(row)

def compatible(r1, r2):
    for i in r1:
        if i in r2:
            return False
    return True

generate_rows([])
Nrows = len(all_rows)
print('rows', Nrows)

compatible_rows = defaultdict(set)
for i in range(Nrows):
    for j in range(i):
        if compatible(all_rows[i], all_rows[j]):
            compatible_rows[i].add(j)
            compatible_rows[j].add(i)
print("compatible_rows done")

@lru_cache(maxsize=100_000)
def count(i, rows_left):
    if rows_left == 1:
        return 1
    return sum(count(j, rows_left - 1) for j in compatible_rows[i])

print(sum(count(i, HEIGHT) for i in range(Nrows)))
