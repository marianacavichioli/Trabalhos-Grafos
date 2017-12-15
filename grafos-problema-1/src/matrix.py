import numpy as np

def getSTM(G):
    # save the adjency matrix

    # init adjacency matrix (amatrix)
    # init result matrix (state transition matrix - stmatrix)
    amatrix = np.array([[0. for i in range(G.number_of_nodes())] for j in range(G.number_of_nodes())])
    lmatrix = np.array([[0. for i in range(G.number_of_nodes())] for j in range(G.number_of_nodes())])

    # create amatrix
    for u, v in G.edges:
        amatrix[int(u)-1][int(v)-1] += 1

    # create pmatrix
    for v in G.nodes():
        lmatrix[int(v)-1][int(v)-1] = 1./float(G.degree((v)))

    stmatrix = np.matmul(lmatrix, amatrix)
    return stmatrix