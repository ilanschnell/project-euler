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
        return 2

    if ((is_black(x0, y0) == is_black(x1, y0) ==
         is_black(x1, y1) == is_black(x0, y1)) and x1 - x0 < size - 1):
        return 2

    if x0 + 1 == x1:
        assert y0 + 1 == y1
        return 1 + 4 * 2

    half = (x1 - x0 + 1) // 2
    return (
        encode(x0,        y0 + half, x1 - half, y1) +
        encode(x0 + half, y0 + half, x1       , y1) +
        encode(x0,        y0       , x1 - half, y1 - half) +
        encode(x0 + half, y0       , x1       , y1 - half) +
        1)

print(encode(0, 0, size - 1, size - 1))
