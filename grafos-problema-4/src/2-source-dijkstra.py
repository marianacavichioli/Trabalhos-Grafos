#!/usr/bin/env python
# -*- coding: utf-8 -*-
import networkx as nx
import numpy as n
import matplotlib.pyplot as plt
import random

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

toggle = True
G = nx.Graph()
j = 0

def Dijkstra(G , vi, vf):
    i = 0
    Q  = {}
    predecessor = {}

    for v,data in G.nodes(data=True):
        Q[v] = np.inf
        predecessor[v] = 'null' 

    for e,x in G.edges():
        if ('weight' not in G[e][x]):
            G[e][x]['weight'] = 1.0   
    
    Q[vi] = 0.0
    predecessor[vi] = None
    Q[vf] = 0.0
    predecessor[vf] = None

    MST  = nx.create_empty_copy(G) 

    while Q:
        u = min(Q,key = Q.get)
        
        for vizinho in G[u]:
        	if vizinho in Q:
        		if Q[vizinho] > Q[u] + G[u][vizinho]['weight']:
        			predecessor[vizinho] = u
        			Q[vizinho] = Q[u] + G[u][vizinho]['weight'] 

        del Q[u]

        if predecessor[u] is not 'null':
            for v1,v2,data in G.edges(data=True):
                if (v1 == predecessor[u] and v2 == u):
                    MST.add_edge(v1,v2, weight=data['weight']) 
                    H = MST.copy() 
                    i = i + 1
                elif (v1 == u and v2 == predecessor[u]):
                    MST.add_edge(v2,v1, weight=data['weight'])
                    H = MST.copy()
                    i = i + 1
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

A = n.loadtxt('wg59_dist.txt')
G = nx.from_numpy_matrix(A)


for v in G.nodes():
	vf = v

vi = 0
vm = vf/2

print(vi, vm, vf)

H = Dijkstra(G, vi, vf, vm)

pos = nx.spring_layout(G)
fig = plt.figure()
fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()


