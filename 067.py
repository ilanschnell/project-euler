triangle = []

for line in open('triangle.txt'):
    triangle.append([int(s) for s in line.split()])

N = len(triangle)

# starting from the second to last row, add the maximum of the two
# elements below to the current element.  Work your way up to the top.
# The result will be the top element.
for r in range(N - 2, -1, -1):
    for c in range(r + 1):
        triangle[r][c] += max(triangle[r + 1][c], triangle[r + 1][c + 1])

print(triangle[0][0])
