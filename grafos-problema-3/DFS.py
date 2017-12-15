#!/usr/bin/env python
# -*- coding: utf-8 -*-
import networkx as nx
import numpy as n
from matplotlib import pyplot as plt

def DFS(G, s):
    cor  = {}
    pred = {}
    d    = {}
    f    = {}

    tempo = 0

    for v in G.nodes():
        cor[v]  = 'branco' # cores possíveis: branco cinza e preto
        pred[v] = None

    for v in G.nodes():
        if cor[v] == 'branco':
            tempo = visit(G, v, cor, pred, d, f, tempo)

    H = nx.create_empty_copy(G)

    for v1,v2 in G.edges():
        if (pred[v2] is v1) or (pred[v1] is v2 and not nx.is_directed(H)):
            H.add_edge( v1, v2 )
            H.node[v1] = d[v1]
            H.node[v2] = d[v2]
            H.node[v1] = f[v1]
            H.node[v2] = f[v2]

    return H

def visit(G, s, cor, pred, d, f, tempo):
    tempo  = tempo + 1
    d[s]   = tempo
    cor[s] = 'cinza'

    for v in G[s]:
        if cor[v] == 'branco':
            pred[v] = s
            tempo = visit(G, v, cor, pred, d, f, tempo)

    cor[s] = 'preto'
    tempo = tempo + 1
    f[s] = tempo

    return tempo

# Cria grafo G
G1 = nx.Graph()
H = nx.Graph()

# Coloca os valores de karate.paj em G
G1 = nx.read_pajek('dolphins.paj')

# Chama método que retorna a DFS-tree
for s in G1.nodes():
    s = '0'
H = DFS(G1, s)

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