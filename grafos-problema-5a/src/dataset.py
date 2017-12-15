import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

# nodes
A = np.loadtxt('./data/ha30_dist.txt')
G = nx.Graph(nx.from_numpy_matrix(A))

# label nodes
L= open('./data/ha30_name.txt').readlines()

i = 0
d = {}
for line in L:
    d[i] = line[:-1]
    i += 1

#print(d)
G=nx.relabel_nodes(G, d)
#print(G.nodes)


#nx.draw(G, with_labels=True)
#plt.show()