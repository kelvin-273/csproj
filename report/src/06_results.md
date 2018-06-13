# Results

We split the results between simulation with $\delta = 1$ for large (undampened) effect of social pressure, and $\delta = 3$ for small (dampened) effect of social pressure.

## Undampened social pressure

Here we simulate the system with the dampening constant set to $\delta = 1$.
We can see from the difference in edge weighting that the edge weights tend toward the extremes over the period of time.

<!--TODO: add visualisations-->

![This is the caption\label{mylabel}](../../../Pictures/Figure_1-0.png)
![This is the caption\label{mylabel}](../../../Pictures/Figure_1-1.png)

We then plot the size of each cluster over the time period and the size of the changes to the groups, i.e. the joint number of people leaving and entering the group at over a time step. These plots show volatility in these values for the whole simulation period. Even when the simulation is run over longer time periods, network still remains volatile, implying that volatility in the social groups is the steady-state behaviour of this system.

<!--TODO: add cluster stat plots-->

![This is the caption\label{mylabel}](../../../Pictures/Figure_1-2.png)
![This is the caption\label{mylabel}](../../../Pictures/Figure_1-3.png)
![This is the caption\label{mylabel}](../../../Pictures/Figure_1-2-1.png)

## Dampened social pressure

Here we simulate the system with the dampening constant set to $\delta = 3$.
As opposed to the undampened case, here we see the edge weights finish the simulation with milder values, i.e. values closer to $0.5$.

<!--TODO: add visualisations-->

![This is the caption\label{mylabel}](../../../Pictures/Figure_2-0.png)
![This is the caption\label{mylabel}](../../../Pictures/Figure_2-1.png)

When we plot the cluster sizes and size of the changes to the social groups. Here, we see that when the system is dampened, there is some change in the social groups but the system eventually converges. 

<!--TODO: add cluster stat plots-->

![This is the caption\label{mylabel}](../../../Pictures/Figure_2-2.png)
![This is the caption\label{mylabel}](../../../Pictures/Figure_2-3.png)
