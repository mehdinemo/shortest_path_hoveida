import networkx as nx
import pandas as pd

city_distances = pd.read_excel('city_distances.xlsx', index_col=0)

G = nx.path_graph(5)
print(nx.shortest_path(G, source=0, target=4))

p = nx.shortest_path(G, source=0)  # target not specified
p[3]  # shortest path from source=0 to target=3

p = nx.shortest_path(G, target=4)  # source not specified
p[1]  # shortest path from source=1 to target=4

p = nx.shortest_path(G)  # source, target not specified
p[2][4]  # shortest path from source=2 to target=4


def mat2edge(mat):
    for