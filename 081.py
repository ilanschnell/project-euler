from networkx import DiGraph, shortest_path_length

matrix = [
    [int(s) for s in line.split(',')]
    for line in open('files/p081_matrix.txt')
]
n = len(matrix)

# Problem 81

G = DiGraph()
for i in range(n):
    for j in range(n):
        w = matrix[i][j]
        G.add_edge((i, j), (i, j + 1), weight=w)  # right
        G.add_edge((i, j), (i + 1, j), weight=w)  # down

source = (0, 0)
target = (n, n - 1)  # target could also be (n - 1, n)
print('p81:', shortest_path_length(G, source, target, weight='weight'))

# Problem 82

for i in range(n):
    # 'source' node has edges to all leftmost "grid" nodes
    G.add_edge('source', (i, 0), weight=0)
    # 'target' node has edges to all rightmost "gird" nodes
    G.add_edge((i, n), 'target', weight=0)
    for j in range(n):
        G.add_edge((i, j), (i - 1, j), weight=matrix[i][j])  # up

print('p82:', shortest_path_length(G, 'source', 'target', weight='weight'))

# Problem 83

for i in range(n):
    for j in range(n):
        G.add_edge((i, j), (i, j - 1), weight=matrix[i][j])  # left

print('p83:', shortest_path_length(G, source, target, weight='weight'))
