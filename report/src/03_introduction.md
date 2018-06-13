
# Introduction

<!--TODO: preamble importance of friendship-->
Having friends is important.
- to resolve issues
- isolation can lead people to insanity
- even social isolation can have the same effect on the brain as physical pain
- What has been done in the field in broad strokes

Modelling social behaviour with networks is a heavily researched field [@Newman2012]. Much research has been done to model individual oriented approaches [@Zeggelink1994] [@Zeggelink1995] where the individuals on the network make concious decisions on who they choose to bee friends with and actor driven behaviour [@VandeBuntG.G.VanDuijnM.A.J.andSnijders1999] similar to similar to individual oriented approaches but where the actors make best statistical guesses based on the constraints of their resources.

In the last decade, since the survey by Schaeffer [@Schaeffer2007], a large amount of research has been done to improve clustering techniques [@Chen2014], [@InternationalConferenceonWorldWideWeb2008], [@VanDongen2000], [@Azad2018].


<!--examples in industry
- Facebook's recommender
- Amazon's recommender
- Ads
- Help in psychology
- 
-->

<!--What's been done in the research so far and why there is a gap-->

<!--
The research can be grouped by these three sections:
- Initialisations of the networks:
  - How the initialised networks imitate the static snapshots of real-life social networks
  - The ease of visualisations of these networks
  - how different network generators can model different kinds of real-life networks
  - The performance characteristics of these networks
  - whether some networks can be approximated by other methods
- Clustering the graphs:
  - local vs global
  - agglomerative vs hierarchical
  - K-Means
  - markov clustering
- Changing the network over time
  - how relationships change over time
  - what we think of the opinions of others
-->


<!--this might be a bit much
rather go at it from the point of view of what has been done in the literature to model the phenomenon
-->

In this work we aim to model a dynamic social network over time and learn how the naturally forming social groups change over time. We simulate this phenomena on random, directed geometric graphs [@Badiu2018] and introduce the notion of social pressure with a controllable dampening effect to change the relationships over time. We then use Markov Clustering algorithm [@VanDongen2000] to determine where the social groups are and measure the size and changes of these groups over time.

The Methods section will show exactly what techniques we employed to derive our answers to our research question. The Results and discussion section will provide the outcomes of our approach, the implications, and ideas for future directions of research.
