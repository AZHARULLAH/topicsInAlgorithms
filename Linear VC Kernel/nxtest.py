import networkx as nx

G = nx.Graph()

# edges = [
#     (1, 2), (1, 3), (1, 4), (2, 4), (3, 4), (3, 5), (4,7), (7, 9), (7, 8), (8, 9), (10, 11), (10, 12), (11, 12)
# ]

edges = [
    (1,3), (1,2), (1,4), (1,5), (5,6)
]

# edges = [
#     (3,5), (7,9), (8,9), (10,12), (11,12)
# ]

# edges = [(1,3), (1,4), (1,2), (3,1), (4,1), (2,1)]

for i in edges:
    G.add_edge(i[0], i[1])
    G.add_edge(i[1], i[0])

# G.add_edges_from([(1,3), (1,4), (1,2), (3,1), (4,1), (2,1)])

print G.number_of_nodes()
print G.number_of_edges()

# print nx.is_bipartite(G)

print nx.maximal_matching(G)

# print nx.is_bipartite(G)
# matching = nx.bipartite.maximum_matching(G)
# print bipartite.maximum_matching(G)
# print matching
