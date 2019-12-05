from numba import njit

size = 1 << 24

@njit
def picture(x, y):
    # picture of a black circle on white background,
    # returns True is pixel x, y is black
    middle = size >> 1
    threshold = middle * middle
    dx = x - middle
    dy = y - middle
    return dx * dx + dy * dy <= threshold

@njit
def encode(x0, y0, x1, y1):
    if x0 == x1:
        assert y0 == y1
        return 2  # color doesn't matter, 2 bits (10 or 11)

    # same color on all four corner -> the whole area is covered by the same
    # color however, this assumption doesn't hold on the first level
    if ((picture(x0, y0) == picture(x1, y0) ==
         picture(x1, y1) == picture(x0, y1)) and x1 - x0 < size - 1):
        return 2  # again: color doesn't matter, 2 bits for entire area

    half = (x1 - x0 + 1) // 2
    return (
        encode(x0,        y0 + half, x1 - half, y1) +
        encode(x0 + half, y0 + half, x1       , y1) +
        encode(x0,        y0       , x1 - half, y1 - half) +
        encode(x0 + half, y0       , x1       , y1 - half) +
        1)  # the single split marker bit

print(encode(0, 0, size - 1, size - 1))
