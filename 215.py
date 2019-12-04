from collections import defaultdict
from functools import lru_cache

WIDTH = 32
HEIGHT = 10

all_rows = []

def generate_rows(row):
    row = list(row)  # need to make a copy here
    p = row[-1] if row else 0  # possition of last crack
    if p + 2 == WIDTH or p + 3 == WIDTH:  # just one brick left?
        all_rows.append(frozenset(row))
        return
    if p + 1 == WIDTH:  # gap too small for a brick?
        return
    # add a small brick
    row.append(p + 2)
    generate_rows(row)
    # replace last 2-brick by 3-brick
    row[-1] += 1
    generate_rows(row)

generate_rows([])
Nrows = len(all_rows)
print('rows', Nrows)

compatible_rows = defaultdict(list)
for i in range(Nrows):
    for j in range(i):
        # rows are compatible when there is no intersection of cracks
        if not (all_rows[i] & all_rows[j]):
            compatible_rows[i].append(j)
            compatible_rows[j].append(i)
print("compatible_rows done")

@lru_cache(maxsize=HEIGHT * Nrows)
def count(i, rows_left):
    if rows_left == 1:
        return 1
    return sum(count(j, rows_left - 1) for j in compatible_rows[i])

print(sum(count(i, HEIGHT) for i in range(Nrows)))
