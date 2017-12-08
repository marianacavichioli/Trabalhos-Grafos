# a) Especifique o diagrama de estados da cadeia
# de Markov que representa o jogo, computando
# para isso a matriz de transição de estados P

import networkx as nx
import matplotlib.pyplot as plt
import sys
sys.path.append("./src")

from dataset import createFromDataset
from matrix import getSTM

# create graph
G = nx.DiGraph()
G = createFromDataset()

# get state transition matrix
P = getSTM(G)

print(nx.info(G))
nx.draw(G)
plt.show()
