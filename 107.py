import networkx

def sum_weights(G):
    return sum(edge[2]['weight'] for edge in G.edges(data=True))

G = networkx.Graph()
for i, line in enumerate(open("files/p107_network.txt")):
    s = line.strip().split(',')
    for j in range(i):
        if s[j] == '-':
            continue
        G.add_edge(i, j, weight=int(s[j]))

print(sum_weights(G) - sum_weights(networkx.minimum_spanning_tree(G)))
