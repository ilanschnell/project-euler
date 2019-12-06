from functools import lru_cache
from bitarray import bitarray as ba, frozenbitarray as fba

# grid size
height = 12
width = 9

# indicate an empty row
EmptyRow = fba(width * [0])

# set a certain bit to one (= position is not available anymore),
# return true if bit was zero
def use(pos, row):
    res = not row[pos]
    row[pos] = 1
    return res

@lru_cache(1 << 20)
def count(rowsLeft, rowA, rowB, rowC):
    if rowsLeft == 0:
        return 1

    # filled another row ?
    if rowA.count() == width:
        return count(rowsLeft - 1, rowB, rowC, EmptyRow)

    # find first gap in rowA
    pos = rowA.index(0)

    result = 0

    # shape: @@
    #        @
    a, b, c = ba(rowA), ba(rowB), ba(rowC)
    if (rowsLeft >= 2 and pos < width - 1 and
            use(pos, a) and use(pos + 1, a) and use(pos, b)):
        result += count(rowsLeft, fba(a), fba(b), fba(c))

    # shape: @@
    #         @
    a, b, c = ba(rowA), ba(rowB), ba(rowC)
    if (rowsLeft >= 2 and pos < width - 1 and
            use(pos, a) and use(pos + 1, a) and use(pos + 1, b)):
        result += count(rowsLeft, fba(a), fba(b), fba(c))

    # shape: @
    #        @@
    a, b, c = ba(rowA), ba(rowB), ba(rowC)
    if (rowsLeft >= 2 and pos < width - 1 and
            use(pos, a) and use(pos, b) and use(pos + 1, b)):
        result += count(rowsLeft, fba(a), fba(b), fba(c))

    # shape:  @
    #        @@
    # note: this shape extends one "negative" unit to the left
    a, b, c = ba(rowA), ba(rowB), ba(rowC)
    if (rowsLeft >= 2 and pos > 0 and
             use(pos, a) and use(pos - 1, b) and use(pos, b)):
        result += count(rowsLeft, fba(a), fba(b), fba(c))

    # shape: @
    #        @
    #        @
    a, b, c = ba(rowA), ba(rowB), ba(rowC)
    if (rowsLeft >= 3 and use(pos, a) and use(pos, b) and use(pos, c)):
        result += count(rowsLeft, fba(a), fba(b), fba(c))

    # shape: @@@
    a, b, c = ba(rowA), ba(rowB), ba(rowC)
    if (rowsLeft >= 1 and pos < width - 2 and
            use(pos, a) and use(pos + 1, a) and use(pos + 2, a)):
        result += count(rowsLeft, fba(a), fba(b), fba(c))

    return result

print(count(height, EmptyRow, EmptyRow, EmptyRow))
