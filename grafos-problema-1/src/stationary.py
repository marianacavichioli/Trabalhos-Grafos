import numpy as np
import sys
sys.path.append("./src")
from matrix import getSTM


def statDist(G, k):
    P = np.array(getSTM(G))                # P0
    w = np.array([0. for j in range(36)])  # w0

    for v in G.nodes(): # creating distribuition vector
        w[int(v)-1] = (float(G.degree(v))/float(2*G.number_of_edges()))

    for i in range(k): # iterating k times (stationary distribuition)
        w = np.matmul(w,P)

    # markov chain prob
    return w