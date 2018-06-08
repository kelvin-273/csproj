# Methods

<!--

Method Layout

- Initialising the graphs
- Iterating the graphs over time
- Clustering the graphs
- Extracting Information out of the graphs
**Why do we choose these approaches?**

-->

In order to evaluate our research question we need to break the procedure into commpartments. In this section we will discuss how we initialise the networks, how we change the networks over time to simulate the changing relationships, how we determine where the social groups and lastly we will discuss how we evaluate our model against real-world data <!--TODO: if we even-->.
In each section we will justify our reasons for using the proposed techniques and attempt to predict how they will affect the dynamics of the network.

## Initialising the graphs

<!--

assumptions about the network
- nodes as people
- edges as relationships
  - [0,1] bad to good
  - [-1,1] bad to good
  - absence of edges to represent not knowing the person

different kinds of social networks
- friendship
- citation
- *the degree distributions of those networks*
assumptions baked into the different kinds of networks
- geometric & distance
- erdos renyi and pure random assignment

-->

## Changing the edges

<!--

- we propose the following method as our iteration method <!--TODO: insert equation-->
- explain the equation
  - original plus some difference
  - calibrating based on the opinions of our friends
  - introducing noise

-->

## Clustering the nodes

<!--

Aim of clustering:
- minimise total distance in cluster vs out cluster
- use equations to explain

Markov Clustering
- clustering by computing the random walks from i to j and pruning the edges until best random walks remain.

-->

## Extracting the information

<!--

This is maybe the most important section
- Visualisation
- Size of each nodes cluster
- Number of people entering and leaving a cluster
  - tracking the cluster by edit distance
    - define this edit distance

-->

## Evaluating against real-world data

<!--

Citation networks

Show different kinds of networks

-->
