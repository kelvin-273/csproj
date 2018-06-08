import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import random
import markov_clustering as mc

from graph_init import *
from graph_iter import *
from graph_clus import *

# Difference Operations --------------------------------------------------------

def diff_op(G, make_chage, diff_f, lens):
    """a higher order function that returns the result of a binary operation
    on based on aspects of the graph before and after some change"""
    a = lens(G)
    make_chage(G)
    b = lens(G)
    val = diff_f(a, b)
    return val

def multi_diff_op(G, make_chage, diff_fs, lens):
    # uses the same lens
    return diff_op(G, make_chage, lambda a, b: [f(a,b) for f in diff_fs], lens)

def edges_change(G):
    """returns the norm of the difference in edges before and after change"""
    def f(a, b):
        # print(a, b, np.array(b) - np.array(b), np.linalg.norm(np.array(b) - np.array(a)))
        return np.linalg.norm(np.array(b) - np.array(a))

    return diff_op(G,
                   update_weights,
                   f,
                   get_weights
                   )
# Analytics --------------------------------------------------------------------

def get_average_weight_per_node(G):
    return [av_weight_of_node(node) for node in G]

def av_weight_of_node(node):
    if len(node) == 0:
        return np.nan
    else:
        return np.mean([node[i]["weight"] for i in node])

# ------------------------------------------------------------------------------

def get_weights(WG):
    return [d["weight"] for (_, _, d) in WG.edges(data=True)]

def plot(G, cluster_map=None):
    """plots the graph w/ or w/out clustering"""

    # sets all nodes to one cluster if cluster_map not given
    if cluster_map == None:
        colors = [0]*len(G.nodes())
    else:
        colors = [cluster_map[i] for i in range(len(G.nodes()))]

    # create edge_cmap
    edge_cmap = plt.cm.coolwarm
    edge_cmap.set_bad("green")
    edge_cmap.set_over("red")
    edge_cmap.set_under("blue")

    fig = plt.figure()
    ax = fig.gca()
    ax.set_facecolor('black')
    # pos=nx.spring_layout(G)
    pos = nx.get_node_attributes(G, 'pos')

    # labels = {i: str(i) for i in G.nodes}



    nx.draw_networkx(G
        , alpha=1
        , with_labels=False
        # , labels=labels
        # , font_size=8
        , pos=pos
        , node_size=24
        , node_color=colors
        , cmap=plt.cm.Set1
        , edge_cmap=edge_cmap
        , edge_color=get_weights(G)
        , edge_alpha=0.2
        , edge_vmin=0
        , edge_vmax=1
        )

    # fig.show()
    plt.show()
    # input("Press Enter")
    # fig.clf()

if __name__ == '__main__':

    lo_clusters = []
    av_cluster_sizes = []
    lo_edges = []

    G = init_random_weighted_geo(100,10)
    clusters = my_clusters(G)
    cluster_map = get_cluster_map(clusters)
    # plot(G, cluster_map)
    for time in range(2):

        lo_clusters.append(clusters)
        av_cluster_sizes.append(av_cluster_size(clusters))
        lo_edges.append(get_weights(G))

        update_weights(G)

        # collect the clusters
        # collect the edge differences

    clusters = my_clusters(G)
    cluster_map = get_cluster_map(clusters)
    # plot(G, cluster_map)
    zero_cls = [my_get_cluster_map(i)[0] for i in lo_clusters]
    size_0_cluster = [len(i) for i in zero_cls]
    distances = [cluster_difference(x, y) for (x, y) in zip(zero_cls[:-1], zero_cls[1:])]
    # size_0_cluster = [len(my_get_cluster_map(i)[0]) for i in lo_clusters]

    # plt.plot(range(1000), size_0_cluster)
    # plt.title("size of node 0s cluster over time")
    # plt.xlabel("time")
    # plt.ylabel("cluster size")
    # plt.show()
    #
    # plt.plot(range(999), distances)
    # plt.title("Number of people entering and leaving 0s cluster over time")
    # plt.xlabel("time")
    # plt.ylabel("Number of people")
    # plt.show()
