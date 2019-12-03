matrix = []
for line in open('matrix-15.txt'):
    line = line.strip()
    if line:
        matrix.append([int(x) for x in line.split()])

n = len(matrix)
assert all(len(matrix[i]) == n for i in range(n))

dp = {0: 0}
dpath = {0: []}

for row_vec in matrix:
    t = {}
    for column in range(n):
        m = 1 << column
        for k in dp:
            if m & k:
                continue
            x = dp[k] + row_vec[column]
            j = m | k
            if x > t.get(j, -1):
                t[j] = x
                dpath[j] = dpath[k] + [column]
    dp = t
    # len(dp) is binomial(n, i), where i is the number of the row 1..n

assert len(dp) == 1
result = dp[(1 << n) - 1]
print(result)

path = dpath[(1 << n) - 1]
print(path)
assert sorted(path) == list(range(n))
assert result == sum(matrix[row][path[row]] for row in range(n))
