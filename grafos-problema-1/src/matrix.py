import numpy as np

def getSTM(G):
    # save the adjency matrix

    # init probability matrix (pmatrix)
    # init adjacency matrix (amatrix)
    # init result matrix (state transition matrix - stmatrix)
    amatrix = np.array([[0. for i in range(G.number_of_nodes())] for j in range(G.number_of_nodes())])
    lmatrix = np.array([[0. for i in range(G.number_of_nodes())] for j in range(G.number_of_nodes())])

    # create amatrix
    edgeFile = open("data/edges", "rt")
    edges = edgeFile.readlines()
    for line in edges:
        amatrix[int(line.split(" ")[0])-1][int(line.split(" ")[1]) - 1] += 1
        amatrix[int(line.split(" ")[1])-1][int(line.split(" ")[0]) - 1] += 1
    edgeFile.close()

    # create pmatrix
    for v in G.nodes():
        lmatrix[int(v)-1][int(v)-1] = 1./float(G.degree((v)))

    stmatrix = np.matmul(lmatrix, amatrix)
    return stmatrix