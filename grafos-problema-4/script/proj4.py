import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import sys
sys.path.append('./src')
from dijkstra2 import dijkstra_2_src

A = np.loadtxt('./WG59/wg59_dist.txt')
G = nx.from_numpy_matrix(A)

T = dijkstra_2_src(G, 1, 5)
#a = np.array([v for v in G.nodes()])

print(nx.info(T))

nx.draw(G)
nx.draw(T)
plt.show()