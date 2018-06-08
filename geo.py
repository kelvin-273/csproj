import networkx as nx
import math
import matplotlib.pyplot as plt
import random
import numpy as np


ave_k = 6           #Wanted average degree
num_nodes = 1000     #Number of nodes
length = 1.         #Size of network domain
density = num_nodes/length      #Density of nodes
radius = math.sqrt(ave_k / (density * np.pi))  #Radius required to get wanted average degree given other values

pos = {i: (random.random(), random.random()) for i in range(num_nodes)}   #Generate positions for nodes

G = nx.random_geometric_graph(num_nodes, radius, pos=pos)       #Generate graph
