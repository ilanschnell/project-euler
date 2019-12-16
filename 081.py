import networkx

matrix = [[int(s) for s in line.split(',')] for line in open('files/p081_matrix.txt')]
n = len(matrix)

# Problem 81

G = networkx.DiGraph()
for i in range(n):
    for j in range(n):
        w = matrix[i][j]
        G.add_edge((i, j - 1), (i, j), weight=w)
        G.add_edge((i - 1, j), (i, j), weight=w)

source = -1, 0
target = n - 1, n - 1
print('p81:', networkx.shortest_path_length(G, source, target, weight='weight'))

# Problem 82

G = networkx.DiGraph()
for i in range(n):
    G.add_edge('source', (i, -1), weight=0)
    G.add_edge((i, n - 1), 'target', weight=0)
    for j in range(n):
        w = matrix[i][j]
        G.add_edge((i, j - 1), (i, j), weight=w)
        G.add_edge((i - 1, j), (i, j), weight=w)
        G.add_edge((i + 1, j), (i, j), weight=w)

print('p82', networkx.shortest_path_length(G, 'source', 'target', weight='weight'))

# Problem 83

G = networkx.DiGraph()
for i in range(n):
    for j in range(n):
        w = matrix[i][j]
        G.add_edge((i, j - 1), (i, j), weight=w)
        G.add_edge((i, j + 1), (i, j), weight=w)
        G.add_edge((i - 1, j), (i, j), weight=w)
        G.add_edge((i + 1, j), (i, j), weight=w)

source = -1, 0
target = n - 1, n - 1
print('p83:', networkx.shortest_path_length(G, source, target, weight='weight'))
