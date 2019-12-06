from functools import lru_cache

# grid size
height = 9
width = 2

# indicate an empty row
EmptyRow = 0

# set a certain bit to one (= position is not available anymore),
# return true if bit was zero
def use(pos, row):
    mask = 1 << pos
    res = bool((row & mask) == 0)
    row |= mask
    return res

@lru_cache
def count(rowsLeft, rowA, rowB, rowC):
    if rowsLeft == 0:
        return 1

    # filled another row ?
    fullRow = (1 << width) - 1
    if rowA == fullRow:
        return count(rowsLeft - 1, rowB, rowC, EmptyRow)

    # find first gap in rowA
    pos = 0
    while (rowA & (1 << pos)) != 0:
        pos += 1

    result = 0

    # shape: ##
    #        #
    a, b, c = rowA, rowB, rowC
    if (rowsLeft >= 2 and pos < width - 1 and
            use(pos, a) and use(pos + 1, a) and use(pos, b)):
        result += count(rowsLeft, a, b, c)

    # shape: ##
    #         #
    a, b, c = rowA, rowB, rowC
    if (rowsLeft >= 2 and pos < width - 1 and
            use(pos, a) and use(pos + 1, a) and use(pos + 1, b)):
        result += count(rowsLeft, a, b, c)

    # shape: #
    #        ##
    a, b, c = rowA, rowB, rowC
    if (rowsLeft >= 2 and pos < width - 1 and
            use(pos, a) and use(pos, b) and use(pos + 1, b)):
        result += count(rowsLeft, a, b, c)

    # shape:  #
    #        ##
    # note: this shape extends one "negative" unit to the left
    a, b, c = rowA, rowB, rowC
    if (rowsLeft >= 2 and pos > 0 and pos < width and
             use(pos, a) and use(pos - 1, b) and use(pos, b)):
        result += count(rowsLeft, a, b, c)

    # shape:  #
    #         #
    #         #
    a, b, c = rowA, rowB, rowC
    if (rowsLeft >= 3 and pos < width and
            use(pos, a) and use(pos, b) and use(pos, c)):
        result += count(rowsLeft, a, b, c)

    # shape: ###
    a, b, c = rowA, rowB, rowC
    if (rowsLeft >= 1 and pos < width - 2 and
            use(pos, a) and use(pos + 1, a) and use(pos + 2, a)):
        result += count(rowsLeft, a, b, c)

    return result

print(count(height, EmptyRow, EmptyRow, EmptyRow))
