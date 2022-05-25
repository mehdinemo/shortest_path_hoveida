import networkx as nx
import pandas as pd
import numpy as np


def main():
    city_distances = pd.read_excel('city_distances.xlsx', index_col=0)
    edges = dis2edge(city_distances)
    G = nx.from_pandas_edgelist(edges, source='source', target='target', edge_attr='weight')
    print(nx.shortest_path(G, source=0, target=4))

    p = nx.shortest_path(G, source=0)  # target not specified
    p[3]  # shortest path from source=0 to target=3

    p = nx.shortest_path(G, target=4)  # source not specified
    p[1]  # shortest path from source=1 to target=4

    p = nx.shortest_path(G)  # source, target not specified
    p[2][4]  # shortest path from source=2 to target=4


def dis2edge(dis):
    s = dis.shape

    if s[0] != s[1]:
        raise ValueError('Incompatible vector size. It must be a binomial '
                         'coefficient n choose 2 for some integer n >= 2.')

    if dis.empty:
        return pd.DataFrame(columns=['source', 'target', 'weight'])

    df_list = []
    st = s[0] - 1
    for index, row in dis.iterrows():
        source = index * st
        source = [source[i:i + len(index)] for i in range(0, len(source), len(index))]
        dic = {'source': source, 'target': row.index[0:st], 'weight': row[0:st]}
        df_list.append(pd.DataFrame(dic))
        st = st - 1
    edge_list = pd.concat(df_list, ignore_index=True)

    return edge_list


if __name__ == '__main__':
    main()
