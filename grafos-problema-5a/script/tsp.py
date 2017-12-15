# -*- coding: utf-8 -*-
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import time
import sys
sys.path.append('./src/')
from twiceAround import twArr

# nodes
A = np.loadtxt('./data/ha30_dist.txt')
G = nx.Graph(nx.from_numpy_matrix(A))

# relabel nodes- to ha30_name names
L= open('./data/ha30_name.txt').readlines()
i = 0
cities = {}
for line in L:
    cities[i] = line[:-1] # get \n out
    i += 1


# TSP execution

# sequential heuristic
pTime = np.array([0. for j in range(len(L))])

for i in range(len(L)):
	# time count test
	beforeProcess = time.clock()
	twArr(G, i).copy()		# subject
	afterProcess = time.clock()
	# end count test

	H = nx.MultiGraph(twArr(G, i).copy())
	pTime[i] = afterProcess - beforeProcess

H = nx.relabel_nodes(H, cities)

# determine 3 best times
pTimeSorted = pTime
pTimeBest3 = np.array([0. for j in range(3)])
pTimeWorst3 = np.array([0. for j in range(3)])
pTimeSorted.sort()

for i in range(len(pTime)):
	if(pTime[i] == pTimeSorted[0]):
		pTimeBest3[0] = i
	elif(pTime[i] == pTimeSorted[1]):
		pTimeBest3[1] = i
	elif(pTime[i] == pTimeSorted[2]):
		pTimeBest3[2] = i

	elif(pTime[i] == pTimeSorted[len(pTime)-1]):
		pTimeWorst3[0] = i
	elif(pTime[i] == pTimeSorted[len(pTime)-2]):
		pTimeWorst3[1] = i
	elif(pTime[i] == pTimeSorted[len(pTime)-3]):
		pTimeWorst3[2] = i

print("""Os menores custos para o caixeiro, em ordem crescente, acontecem quando se parte de:
{}, {} e {}
 """.format(cities[pTimeBest3[0]],cities[pTimeBest3[1]],cities[pTimeBest3[2]]))

print("""Os maiores custos para o caixeiro, em ordem decrescente, acontecem quando se parte de:
{}, {} e {}
 """.format(cities[pTimeWorst3[0]],cities[pTimeWorst3[1]],cities[pTimeWorst3[2]]))

print("""A diferença entre o melhor e o pior custo para o caixeiro é de {} segundos.
	""".format( pTime[int(pTimeWorst3[0])] - pTime[int(pTimeBest3[0])] ) )
# - pTime[pTimeBest3[0]]) 