import networkx as nx
import numpy as np
from matplotlib import pyplot as plt

G = nx.read_pajek('karate.paj') #coloca o grafo do arquivo em G
r = 1 #vertice raiz

def BFS(G,s): 
    cor = {} #declara vetor de cores
    pred = {} 
    d = {}
    for v in G.nodes():
        Q[v] = np.inf
        cor[v] = 'branco'
        pred[v] = None
    cor[s] = 'cinza'
    d[s] = 0
    Q = [s]
    while Q:
        u = Q.pop(0)
        for v in G.neighbors(u):
            if cor[v] == 'branco':
                cor[v] = 'cinza'
                d[v] = d[u] + 1
                pred[v] = u
                Q.append(v)
        cor[u] = 'preto'
    H = nx.create_empty_copy(G)
    for v1,v2,data in G.edges(data=True):
        if (pred[v2] is v1) or (pred[v1] is v2 and not nx.is_directed(H)):
            H.add_edge(v1,v2,data)
            H.node[v1]['depth'] = d[v1]
            H.node[v2]['depth'] = d[v2]
    return H



H = BFS(G,1)
nx.draw_networkx(G)
plt.savefig('BFS_karate.pdf')
plt.show()
