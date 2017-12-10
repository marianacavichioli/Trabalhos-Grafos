import numpy as np
# relax primitive
def relax(u, v, G, sp, n):
    if(sp[v] > sp[u] + G.get_edge_data(u,v)['weight']):
        sp[v] = sp[u] + G.get_edge_data(u,v)['weight']
        n[v] = u
        return np.array([sp, n])

    return np.array([])