
# -*- coding: utf-8 -*-

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

toggle = True
G = nx.Graph()
j = 0

def Prim(G = nx.Graph(), R = None):
    i = 0
    Q  = {}
    predecessor = {}

    for v,data in G.nodes(data=True):
        Q[v] = np.inf
        predecessor[v] = 'null'    
    
    Q[R] = 0.0 
    MST  = nx.create_empty_copy(G) 

    while Q:
        u = min(Q,key = Q.get)
        del Q[u]
        
        for vizinho in G[u]:
            if vizinho in Q:
                if G[u][vizinho]['weight'] < Q[vizinho]:
                    predecessor[vizinho] = u 
                    Q[vizinho] = G[u][vizinho]['weight'] 

        if predecessor[u] is not 'null':
            for v1,v2,data in G.edges(data=True):
                if (v1 == predecessor[u] and v2 == u):
                    MST.add_edge(v1,v2, weight=data['weight']) 
                    H = MST.copy() 
                elif (v1 == u and v2 == predecessor[u]):
                    MST.add_edge(v2,v1, weight=data['weight'])
                    H = MST.copy()
    return H

def onclick(event):
    global toggle
    global j
   
    event.canvas.figure.clear()

    if toggle:
        labels = {}
        for v1,v2,data in G.edges(data=True):
            labels[(v1,v2)] = data['weight']
        nx.draw(G, pos, with_labels=True)
        nx.draw_networkx_edge_labels(G, pos, labels)
        toggle = not toggle
    
    else:
        labels = {}
	for v1,v2,data in H.edges(data=True):
            labels[(v1,v2)] = data['weight']
        nx.draw(H, pos, with_labels=True)
        nx.draw_networkx_edge_labels(H, pos, labels)

    event.canvas.draw()

A = np.loadtxt('ha30_dist.txt')
G = nx.from_numpy_matrix(A)

H = Prim(G, 0)

pos = nx.spring_layout(G)
fig = plt.figure()
fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()
