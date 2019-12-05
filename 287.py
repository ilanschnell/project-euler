from numba import njit

size = 1 << 24

@njit
def is_black(x, y):
    middle = size >> 1
    threshold = middle * middle
    dx = x - middle
    dy = y - middle
    return dx * dx + dy * dy <= threshold

@njit
def encode(x0, y0, x1, y1):
    if x0 == x1:
        assert y0 == y1
        return 2  # color doesn't matter, always 2 bits


    # same color on all four corner -> the whole area is covered by the same
    # color however, this assumption doesn't hold on the first level
    if ((is_black(x0, y0) == is_black(x1, y0) ==
         is_black(x1, y1) == is_black(x0, y1)) and x1 - x0 < size - 1):
        return 2

    # optimisaztion: if a 2x2 area needs to be split, then it always
    # requires 9 bits (a split bit and 4 color bits)
    if x0 + 1 == x1:
        assert y0 + 1 == y1
        return 9

    half = (x1 - x0 + 1) // 2
    return (
        encode(x0,        y0 + half, x1 - half, y1) +
        encode(x0 + half, y0 + half, x1       , y1) +
        encode(x0,        y0       , x1 - half, y1 - half) +
        encode(x0 + half, y0       , x1       , y1 - half) +
        1)

print(encode(0, 0, size - 1, size - 1))
