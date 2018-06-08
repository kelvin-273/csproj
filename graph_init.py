"""functions to generate random networks"""

import numpy as np
import networkx as nx
import random

def init_random_weighted(n, p):
    # net = nx.gnp_random_graph(n, p, directed=True)
    DG = nx.random_geometric_graph(n,p)
    DG = make_bidirectional(DG)
    add_random_weights(DG)
    # DG = nx.DiGraph([(u,v,{'weight':random.random()}) for (u,v) in net.edges()])
    return DG

def init_random_weighted_geo(n, k):
    """generate a random geometric network with average degree of k"""
    # TODO: clean the comments
    length = 1        # Size of network domain
    density = n/length      # Density of nodes
    radius = np.sqrt(k / (density * np.pi))  # Radius required to get wanted average degree given other values

    # Generate positions for nodes
    pos = {i: (random.random(), random.random()) for i in range(n)}

    G = nx.random_geometric_graph(n, radius, pos=pos)       #Generate graph
    G = make_bidirectional(G)
    add_random_weights(G)
    return G

def add_random_weights(G):
    """gives a graph random weights"""
    for (_,_,d) in G.edges(data=True):
        d["weight"] = random.random()

def make_bidirectional(G):
    return nx.DiGraph(G)
