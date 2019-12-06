from functools import lru_cache

DIGITS = 40

# initial mask for no digits set
no_digits = 0
# mask for all digits set
all_digits = (1 << 10) - 1

@lru_cache(1024 * 10 * DIGITS)
def count(mask, curr, digits_left):
    """
    count pandigital step numbers where bits in mask are set according
    to the first digits
    """
    mask |= 1 << curr

    if digits_left == 0:
        # if all ten bits are set, we have a pandigital
        return mask == all_digits

    res = 0
    if curr > 0:  # next digit is smaller
        res += count(mask, curr - 1, digits_left - 1)
    if curr < 9:  # next digit is bigger
        res += count(mask, curr + 1, digits_left - 1)
    return res

result = 0
for num_digits in range(DIGITS):
    for digit in range(1, 10):  # first digit cannot be 0, only 1..9
        result += count(no_digits, digit, num_digits)
print(result)
