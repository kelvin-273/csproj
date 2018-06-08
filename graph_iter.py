import numpy as np
import networkx as nx

# Iterate Graph ----------------------------------------------------------------

def update_weights(G):
    nodes = G.nodes()
    updates = {i: new_weights_i(G, i) for i in nodes}
    for i in nodes:
        for j in G[i]:
            # print(i, j, updates[i][j], sep=' <> ')
            G[i][j]["weight"] = updates[i][j]
    print('blah')
    print(updates)

def update_weights2(G):
    E = nx.to_numpy_array(G)

    # collect boolean matrix that represents

    num = (sum(E**2) - E @ E)
    den = sum(E)

    shift = num / den



def new_weights_i(G, i):
    return {j: new_weight_ij(G, i, j) for j in G[i]}

def new_weight_ij(G, i, j):
    e = lambda a, b: G[a][b]["weight"]
    numerator = np.sum([e(i,k)*(e(k,j) - e(i,j)) for k in G[i] if k != j and G[k].get(j)])
    denominator = np.sum([e(k,j) for k in G[i] if k != j and G[k].get(j)])
    # catch divide by zero error
    if denominator == 0:0, (1 - (e(i,j) - 0.5)**2) / 2)
        out = e(i,j)
    else:
        out = e(i,j) + numerator / denominator

    # add gaussian
    perturb = np.random.normal(0, (1 - (e(i,j) - 0.5)**2) / 2)
    # print("perturb:", perturb)
    out += perturb

    # bound between 0 and 1
    if out < 0:
        out = 0
    elif out > 1:
        out = 1
    # print(out)
    return out
