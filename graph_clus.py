import networkx as nx
import numpy as np
import markov_clustering as mc

# Cluster the Graph ------------------------------------------------------------

def my_clusters(G):
    matrix = nx.to_scipy_sparse_matrix(G)
    results = mc.run_mcl(matrix)
    clusters = mc.get_clusters(results)
    return clusters

def get_cluster_map(clusters):
    """
    returns a dictionary that maps a node to a unique the index of its cluster
    """
    return {node: i for i, cluster in enumerate(clusters) for node in cluster}
    # colors = [cluster_map[i] for i in range(len(G.nodes()))]

def my_get_cluster_map(clusters):
    return {node: cluster for cluster in clusters for node in cluster}

def gets_k_clusters(i, lo_clusters):
    return [my_get_cluster_map(ix)[i] for ix in lo_clusters]

# Cluster Size -----------------------------------------------------------------

def av_cluster_size(clusters, G=None):
    if G:
        return len(G.nodes()) / len(clusters)
    else:
        sum(map(len, clusters)) / len(clusters)

# Cluster Stability ------------------------------------------------------------

def cluster_difference(c0, c1):
    """returns the number of nodes that have entered and left between 2 t-steps"""
    s0, s1 = set(c0), set(c1)
    return len(s0.symmetric_difference(s1))

if __name__ == '__main__':
    from graph_init import *

    # Create test cases
    
