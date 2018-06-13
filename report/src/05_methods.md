# Methods

<!--

Method Layout

- Initialising the graphs
- Iterating the graphs over time
- Clustering the graphs
- Extracting Information out of the graphs
**Why do we choose these approaches?**

-->

In order to evaluate our research question we need to break the procedure into compartments. In this section we will discuss how we initialise the networks, how we change the networks over time to simulate the changing relationships, how we determine where the social groups emerge and lastly we will discuss how we extract information from the network to answer our proposed research question.
In each section we will justify our reasons for using the proposed techniques and attempt to predict how they will affect the dynamics of the network.

## Initialising the graphs

<!--

assumptions about the network
- nodes as people
- edges as relationships
  - [0,1] bad to good
  - [-1,1] bad to good
  - absence of edges to represent not knowing the person

-->

To start, we make some assumptions about the how we represent the social network using graphs. Let $G = (V,E)$ represent the network where $V$ is the set of nodes in the network and $E \in V \times V$ are the edges that connect one node to another. We use the nodes of the graph to represent the people in the network and the edges to represent the opinions such that edge $(u,v,w) \in E$ represents the opinion that person $u$ holds of person $v$ and $w$ is the magnitude of that opinion. We set $w$ to a real numerical value $w \in [0,1]$ where lower values represent bad opinions and higher values represent good opinions. These relationships are unfortunately not always mutual in the real world, but rather directional. We use directional graph where every relationship can represented by a pair of two edges such that $\forall u,v\in V,\ (u,v,w_{1})\in E\implies(v,u,w_{2})\in E$.

In this project we make the assumption that as people are largely constrained to their location, so too are their relationships.
As such, we initialise the network as a random geometric graph with random with random edge weights in our specified domain, and control over the average degree and the number of nodes in the network.
The use of random geometric networks also makes the visualisation process much easier than other graphs, as one can use the positions of the nodes that the graph was initialised with to get a neat graphical representation.

## Changing the edges

<!--

- we propose the following method as our iteration method TODO: insert equation
- explain the equation
  - original plus some difference
  - calibrating based on the opinions of our friends
  - introducing noise

-->

In our model, we make the assumption that a opinion is dependent on the opinions of their peers. Whilst this may not always be the case, studies do show this to be a factor that contributes to group behaviour<!--TODO: cite-->. We decided to model the changing relationships over discrete time steps and at each time steps to reduce the complexity of the model. At each time step, the edge weights change according to the following rule:
$$
e_{t+1}(i,j) = e_t(i,j) + 
\dfrac{\sum_{k\ne j}e_{t}(i,k)(e(k,j)-e(i,j))}{\delta\sum_{k\ne j}e(i,k)}
$$
where $e_{t}(i,j)$ is the weight of the edge between nodes $i$ and
$j$ at time $t$; $k$ is a neighbour of $i$ that is not $j$ and $\delta$ is a dampening constant that limits the effect of social pressure on the edges. The
numerator represents the weighted sum of all the differences in opinion
about person $j$ between person $i$ and the neighbours of person
$i$. The denominator is a scaling factor that ensures that the final
value of $e_{t+1}(i,j)$ remains the domain $[0,1]$ as long as $\delta > 1$.

## Clustering the nodes

<!--

Aim of clustering:
- minimise total distance in cluster vs out cluster
- use equations to explain

Markov Clustering
- clustering by computing the random walks from i to j and pruning the edges until best random walks remain.

-->

Clustering the graph allows us to see where the social structures lie and which people are in the social groups. There many different methods of clustering that ask different questions [@Schaeffer2007]. 
For this project we require a clustering method that assigns each node to a cluster where the number of clusters created is not fixed by the user, like K-Means Clustering, but inferred from the properties of the network.
We also require a method whose cluster sizes are not dependent on the scope at which the relationship is observed. By example, Hierarchical Clustering recursively clusters pairs of clusters starting from individual nodes in a tree-like structure .
Lastly we need a clustering algorithm that can scale to large networks. Clustering is $\mathcal{NP}$-Hard and we need to perform the clustering at every time step, so the accumulative effect of solving these problems to optimality would be infeasible for the scope of this project. Approximation algorithms become very useful in this regard as they trade accuracy for efficiency.

In this experiment we used Markov Clustering [@VanDongen2000], which repeatedly computes the random walks from each node in the network to every other node and prunes the walks with low probability until there is no change in cluster assignments.
This method creates clusters that are naturally forming and whose number are not arbitrarily set. While this algorithm is not polynomial time algorithm, Van Dongen's PhD dissertation includes a proof that the algorithm converges to a steady state.

At each time step we use this algorithm on the network to generate a list of clusters where each cluster is a list of nodes. Over the execution of the program, we collect these lists of clusters to be processed for information extraction.

## Extracting the information

<!--

This is maybe the most important section
- Visualisation
- Size of each nodes cluster
- Number of people entering and leaving a cluster
  - tracking the cluster by edit distance
    - define this edit distance

-->

Thus far we have discussed the methods we will use to initialise and simulate the graph over time, but in order to answer our original question, we need to be able to extract information about the network in the form of numerical values. 
The question originally posed, asked how the social groups on a social network change over time. 
So we need to be able to measure aspects about the clusters over time. 
At the start and end of the simulation we create visualisations of the networks. In these visualisations, the edge weights are
In this experiment we looked at the size of the different social groups and the number of people entering and leaving the social group over time.

<!--TODO: justify why no real-world data-->

