import networkx as nx # import networkx lib

def createFromDataset():
    # create digraph
    G = nx.Graph()

    # create edges
    edgeFile = open("data/edges", "rt")
    edges = edgeFile.readlines()
    # create nodes  
    for v in edges:
        G.add_node(int(v.split(" ")[0]))
        G.add_node(int(v.split(" ")[1]))

    for line in edges:
        G.add_edge(int(line.split(" ")[0]), int(line.split(" ")[1]))


    edgeFile.close()

    return G