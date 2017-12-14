import networkx as nx
import numpy as np
import matplotlib.pylab as plt
import sys
sys.path.append('./src/')
from Prim import Prim



def twArr(G, src):
    H = nx.Graph()
    T = nx.MultiGraph(Prim(G, src).copy())
    for e in list(T.edges):
        T.add_edge(e[0], e[1], weight=G[e[0]][e[1]]['weight'])
    L = np.array(list(nx.eulerian_circuit(T, src)))

    LNodes = list()
    LNoRepeat = list()
    for u, v in L:
        LNodes.append(u)
        LNodes.append(v)

    for vk in LNodes:
        if((vk not in LNoRepeat) or(len(LNoRepeat) == 0)):
            LNoRepeat.append(vk)

    for v in range(len(LNoRepeat)):
        if(v is not len(LNoRepeat)-1):
            H.add_edge(
                LNoRepeat[v],
                LNoRepeat[v+1],
                weight=G[LNoRepeat[v]][LNoRepeat[v+1]]['weight']
                )
        else:
            H.add_edge(
                LNoRepeat[v],
                LNoRepeat[0],
                weight=G[LNoRepeat[v]][LNoRepeat[0]]['weight']
                )

    return H