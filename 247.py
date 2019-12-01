from math import sqrt
from heapq import heappush, heappop

class Square(object):
    def __init__(self, x0, y0, left, below):
        self.x0 = x0
        self.y0 = y0
        self.s = 0.5 * (sqrt((x0 - y0) ** 2 + 4) - x0 - y0)
        self.x1 = x0 + self.s
        self.y1 = y0 + self.s
        self.left = left
        self.below = below

    def __lt__(self, other):
        return self.s > other.s

indexLeft = 3
indexBelow = 3
result = 0
todo = []
heappush(todo, Square(1, 0, 0, 0))
candidates = 1
while candidates:
    result += 1
    current = heappop(todo)
    upper = Square(current.x0, current.y1, current.left, current.below + 1)
    right = Square(current.x1, current.y0, current.left + 1, current.below)
    heappush(todo, upper)
    heappush(todo, right)
    if upper.left <= indexLeft and upper.below <= indexBelow:
       candidates += 1
    if right.left <= indexLeft and right.below <= indexBelow:
       candidates += 1
    if current.left <= indexLeft and current.below <= indexBelow:
       candidates -= 1
print(result)
