#!/usr/bin/env python
#-*- coding: utf-8 -*-
import networkx as nx
import numpy as n
from matplotlib import pyplot as plt

def BFS(G,s): 
    cor = {} #declara vetor de cores
    pred = {} 
    d = {}
    for v in G.nodes():
        d[v] = n.inf
        cor[v] = 'branco'
        pred[v] = None
    cor[s] = 'cinza'
    d[s] = 0
    Q = [ s ]
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
    for v1,v2 in G.edges():
        if (pred[v2] is v1) or (pred[v1] is v2 and not nx.is_directed(H)):
            H.add_edge( v1,v2 )
            H.node[v1] = d[v1]
            H.node[v2] = d[v2]
    return H

# Cria grafo G
G1 = nx.Graph()
H = nx.Graph()

# Coloca os valores de karate.paj em G
G1 = nx.read_pajek('dolphins.paj')

# Chama método que retorna a BFS-tree
for s in G1.nodes():
    s = '0'
H = BFS(G1, s)

# Salva as profundidades cada nó de H em labels
labels = {}
for v in H.nodes():
    labels[v] = H.node[v]

# Retorna um dicionário de posições codificadas por nó
pos = nx.spring_layout(H)

# Desenha o grafo H
nx.draw(H, pos)

# Desenha com as arestas e labels
nx.draw_networkx_labels(H, pos, labels)
nx.draw_networkx_edges(H, pos)

# Exibe
plt.show()
