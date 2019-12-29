from itertools import count

def recur_length(d):
    r = 1
    seen = {}
    for i in count(0):
        if r == 0:
            return 0
        if r in seen:
            return i - seen[r]
        seen[r] = i
        r = (10 * r) % d

assert recur_length(7) == 6

length, d = max((recur_length(d), d) for d in range(2, 1000))
print(d)
