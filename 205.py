import itertools
from collections import Counter


def count_totals(s, n):
    """
    Given the number of sides (s), and number of dice (n),
    count the totals for all possible dice comibnations, and return a dictionary
    mapping the total to the number of occurrences.
    """
    return Counter(sum(r) for r in
                   itertools.product(range(1, s+1), repeat=n))

# In the following player 1 is Peter with his 9 four-sided dice,
# ans player 2 is Colin with his 6 six-sided dice.
res = 0
for t1, c1 in count_totals(4, 9).items():
    for t2, c2 in count_totals(6, 6).items():
        if t1 > t2:  # player 1 wins
            res += c1 * c2
res /= pow(4, 9) * pow(6, 6)
print('%.7f' % res)
