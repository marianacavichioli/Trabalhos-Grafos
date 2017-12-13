import networkx as nx
import numpy as n
from matplotlib import pyplot as plt

def BFS(G, s):
    cor  = {}
    pred = {}
    d    = {}

    for v in G.nodes():
        d[v]    = n.inf
        cor[v]  = 'branco' # branco cinza e preto
        pred[v] = None

    cor[s]  = 'cinza'
    d[s]    = 0

    Q = [ s ]

    while Q:
        u = Q.pop(0)
        for v in G.neighbors(u):
            if cor[v] == 'branco':
                cor[v]  = 'cinza'
                d[v]    = d[u] + 1
                pred[v] = u

                Q.append(v)

        cor[u] = 'preto'

    H = nx.create_empty_copy(G)

    for v1,v2,data in G.edges(data=True):
        if (pred[v2] is v1) or (pred[v1] is v2 and not nx.is_directed(H)):
            H.add_edge( v1, v2, data )
            H.node[v1]['depth'] = d[v1]
            H.node[v2]['depth'] = d[v2]

    return H

G = nx.Graph()

G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)
G.add_node(6)
G.add_node(7)
G.add_node(8)
G.add_node(9)
G.add_node(10)
G.add_node(11)
G.add_node(12)
G.add_node(13)
G.add_node(14)
G.add_node(15)
G.add_node(16)
G.add_node(17)
G.add_node(18)
G.add_node(19)
G.add_node(20)
G.add_node(21)
G.add_node(22)
G.add_node(23)
G.add_node(24)
G.add_node(25)
G.add_node(26)
G.add_node(27)
G.add_node(28)
G.add_node(29)
G.add_node(30)
G.add_node(31)
G.add_node(32)
G.add_node(33)
G.add_node(34)

G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 3)
G.add_edge(1, 4)
G.add_edge(2, 4)
G.add_edge(3, 4)
G.add_edge(1, 5)
G.add_edge(1, 6)
G.add_edge(1, 7)
G.add_edge(5, 7)
G.add_edge(6, 7)
G.add_edge(1, 8)
G.add_edge(2, 8)
G.add_edge(3, 8)
G.add_edge(4, 8)
G.add_edge(1, 9)
G.add_edge(3, 9)
G.add_edge(3, 10)
G.add_edge(1, 11)
G.add_edge(5, 11)
G.add_edge(6, 11)
G.add_edge(1, 12)
G.add_edge(1, 13)
G.add_edge(4, 13)
G.add_edge(1, 14)
G.add_edge(2, 14)
G.add_edge(3, 14)
G.add_edge(4, 14)
G.add_edge(6, 17)
G.add_edge(7, 17)
G.add_edge(1, 18)
G.add_edge(2, 18)
G.add_edge(1, 20)
G.add_edge(2, 20)
G.add_edge(1, 22)
G.add_edge(2, 22)
G.add_edge(24, 26)
G.add_edge(25, 26)
G.add_edge(3, 28)
G.add_edge(24, 28)
G.add_edge(25, 28)
G.add_edge(3, 29)
G.add_edge(24, 30)
G.add_edge(27, 30)
G.add_edge(2, 31)
G.add_edge(9, 31)
G.add_edge(1, 32)
G.add_edge(25, 32)
G.add_edge(26, 32)
G.add_edge(29, 32)
G.add_edge(3, 33)
G.add_edge(9, 33)
G.add_edge(15, 33)
G.add_edge(16, 33)
G.add_edge(19, 33)
G.add_edge(23, 33)
G.add_edge(24, 33)
G.add_edge(30, 33)
G.add_edge(31, 33)
G.add_edge(32, 33)
G.add_edge(9, 34)
G.add_edge(10, 34)
G.add_edge(14, 34)
G.add_edge(15, 34)
G.add_edge(16, 34)
G.add_edge(19, 34)
G.add_edge(21, 34)
G.add_edge(23, 34)
G.add_edge(24, 34)
G.add_edge(27, 34)
G.add_edge(28, 34)
G.add_edge(29, 34)
G.add_edge(30, 34)
G.add_edge(31, 34)
G.add_edge(32, 34)
G.add_edge(33, 34)

H = BFS(G, 1)

labels = {}
for v in H.nodes():
    labels[v] = H.node[v]

pos = nx.spring_layout(H)
nx.draw(H, pos)
# pos = nx.spring_layout(G)
# nx.draw(G, pos)
#nx.draw_networkx_labels(H, pos, labels)
#nx.draw_networkx_edges(H, pos)

plt.savefig('DFS_karate.pdf')
plt.show()