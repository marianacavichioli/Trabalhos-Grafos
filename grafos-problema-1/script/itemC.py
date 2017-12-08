import networkx as nx
import numpy as np
import sys
sys.path.append('./src')
from dataset import createFromDataset
from stationary import statDist

G = createFromDataset()

# Especifique a matriz P_ (P_barra) referente ao modelo Pagerank considerando alpha = 0.1.
P_ = nx.google_matrix(G, alpha=0.1)
print(P_)

#Considerando k = 100, aplique o Power method e compare o resultado com o obtido no item b).
#  As distribuições estacionárias obtidas em b) e c) são iguais ou diferentes?

# distribuição estacionaria item C
wdict = nx.pagerank(G, alpha=0.1, max_iter=100)
witemC = [0.for i in range(len(P_))]

for key in wdict:
    witemC[key-1]= wdict[key]

# distribuição estacionária item B
witemB = statDist(G, 100)

# Comparar vetores:
isDif = False # booleana para diferentes
contDif = 0 # contador para os diferentes

for i in range(len(witemB)):
    if(witemB[i] != witemC[i]):
        if(~isDif): isDif = True
        contDif += 1

if(isDif):
    print("\nSao diferentes, com "+str(contDif)+" vertices diferentes.\n")
else:
    print("\nSao iguais.\n")