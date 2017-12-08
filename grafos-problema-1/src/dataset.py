import networkx as nx # import networkx lib

def createFromDataset():
    # create digraph
    G = nx.Graph()

    # create nodes
    for i in range(1,37):
        G.add_node(i)

    # create edges
    edgeFile = open("data/edges", "rt")
    edges = edgeFile.readlines()

    for line in edges:
        G.add_edge(int(line.split(" ")[0]), int(line.split(" ")[1]))
    edgeFile.close()

    return G