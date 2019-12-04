from collections import defaultdict
from functools import lru_cache

WIDTH = 32
HEIGHT = 10

all_rows = []

def generate_rows(row):
    p = row[-1] if row else 0  # possition of last crack
    if WIDTH - p in (2, 3):
        # just one brick left, so append this one to our list
        all_rows.append(frozenset(row))
        return
    if WIDTH - p == 1:
        # gap too small for another brick
        return
    row = list(row)  # need to copy before modifying
    # add a small brick
    row.append(p + 2)
    generate_rows(row)
    # replace last 2-brick by 3-brick
    row[-1] += 1
    generate_rows(row)

generate_rows([])
N = len(all_rows)
print('rows', N)

compatible_rows = defaultdict(list)
for i in range(N):
    for j in range(i):
        # rows are compatible when there is no intersection of cracks
        if not (all_rows[i] & all_rows[j]):
            compatible_rows[i].append(j)
            compatible_rows[j].append(i)
print("compatible_rows done")

@lru_cache(maxsize=HEIGHT * N)
def count(i, remaining_rows):
    if remaining_rows == 1:
        return 1
    return sum(count(j, remaining_rows - 1) for j in compatible_rows[i])

print(sum(count(i, HEIGHT) for i in range(N)))
