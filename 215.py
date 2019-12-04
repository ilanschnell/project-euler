from collections import defaultdict
from itertools import product
from functools import lru_cache

WIDTH = 32
HEIGHT = 10

def generate_rows():
    result = set()
    for s in product(range(2), repeat=WIDTH // 2):
        bricks = [3 if k else 2 for k in s]
        row = []
        p = 0
        for w in bricks:
            p += w
            if p > WIDTH:
                break
            if p == WIDTH:
                result.add(frozenset(row))
            row.append(p)
    return sorted(result)

def compatible(r1, r2):
    for i in r1:
        if i in r2:
            return False
    return True

rows = generate_rows()
Nrows = len(rows)
print('rows', Nrows)

compatible_rows = defaultdict(set)
for i in range(Nrows):
    for j in range(i):
        if compatible(rows[i], rows[j]):
            compatible_rows[i].add(j)
            compatible_rows[j].add(i)
print("compatible_rows done")

@lru_cache(maxsize=100_000)
def count(i, rows_left):
    if rows_left == 1:
        return 1
    return sum(count(j, rows_left - 1) for j in compatible_rows[i])

print(sum(count(i, HEIGHT) for i in range(Nrows)))
