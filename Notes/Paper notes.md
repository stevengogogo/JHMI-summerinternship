# Paper notes
> [name=Shao-Ting Chiu]
> [time=Thu, Jun 21, 2018 2:02 PM]

# Mitochondrial network complexity emerges from fission/ fusion dynamics

Paper: [link](https://www.nature.com/articles/s41598-017-18351-5)

## Overview

> A recent model of mitochondrial dynamics suggested that mitochondria networks are poissed at the **critical point** of a phase transition.

> No connection between theory and phenomenology has been provided yet.


```flow

st=>start: Confocal microscopy images
e=>end: link between theory and experiments
op=>operation: network
op2=>operation: percolation theory
op3=>operation: extract parameters

st->op->op2->op3->e
```
## Results

### Pipeline

|Matlab function|function|content|
|---|---|---|
||im2bw|convertion of a grayscale image into a binary imag.|
||bwmorph|binarized versoins of the image were transformed into skeletons of uniform|
||bwlabel|extract clusters|
||boxcount|fractal dimension|
||komogorov|Kolmogorov complexity is a better way to measure network complexity than Shannon's enrtopy ([ref](https://www.hindawi.com/journals/complexity/2017/3250301/#B27))|
||entropy|Entropy|

:::info
**What is [bwlabel](https://www.mathworks.com/help/images/ref/bwlabel.html#bupqqy6-1-BW) doing?**

```
L = bwlabel(Binary_image, connected_number)
```
Label connected components in 2-D binary image
![](https://i.imgur.com/QlQXYU7.png)
![](https://i.imgur.com/oZiIaEi.png)
:::



:::success
**Thinking further** 

Although mitochondrial networks are embeded in the 3-dimensional cellular volume, artefactual branching points in 2-dimensional reconstrucions were negligible.
:::

### Parameters from skeletons

|Parameter|Description|
|---|---|
|Cluster mass(s)|counting the number of pixels in each individual cluster|
|pixel degree(k)|counting the nearest neighbors of each pixel|

## Methods

### Image analysis

```flow

st=>start: imaging fluorescent tagged mitochondria
e=>end: clurtering (bwlabel)
op=>operation: 8-bit images -> binary (im2bw)
op2=>operation: skeletonization (bmorph)

st->op->op2->e

```

### Mitochondria network perturbation

|Gene|modification|effect|
|---|---|---|
|pqt||increasing fission|
|mfn|over-expression|promoting fusion|

## :question: What is percolation theory?

Percolation theory deals with the numbers and properties of the clusters formed when sites are occupied with probability $p$

see [Percolation theory](http://web.mit.edu/ceder/publications/Percolation.pdf)

:::info
**Definition**
The percolation threshold $p_{c}$ is the concentration (occupation probability) p at which an infinite cluster appears for the first time in an infinite lattice
:::

## :question: Why does p(s) exhibited a power law behavior that seemed to be robust against threshold variations?

see [Power-Law Distributions in Empirical Data](https://epubs.siam.org/doi/pdf/10.1137/070710111)
and [a finite size scaling analysis](https://journals.aps.org/prl/pdf/10.1103/PhysRevLett.113.238102)

## [Sukhorukov et al. model](http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1002745)

### Fission-Fussion process

In the model, a dimer tip can connect (disconnect) to other dimer tips forming a network node, but at most three tips can be merged.

Let $X_{\kappa}$ denotes the node with degree $\kappa$,

$$2X_{1}\leftrightarrow_{b_{1}}^{a_{1}} X_{2}$$

$$X_{1} + X_{2} \leftrightarrow_{b_{2}}^{a_{2}}X_{3}$$

### Simulation
Gillespie algorithm

### Asumption in this paper

$$b_{2} = \frac{3}{2}b_{1}$$

$$c_{i} = \frac{a_{i}}{b_{i}}$$

### Simulation in this paper

Roughly the estimated value for the average number of edges in control netwroks, L=15000


### Network features

|Feature|notation|
|---|---|
|average degree|$\kappa$|
|average fraction of nodes in the largest cluster|$\frac{N_{g}}{N}$|
|average cluster size excluding the largest cluster|$s$|


# How I think about this paper?

This paper is very similar to [what I tried to do](https://drive.google.com/open?id=0B0fatyRgBBHgaDR2MFZ4T090WUk) in BMES conference. There are several key points of this article:

1. Use Kolmogorov complexity to measure the complexity of networks provide a gereral view on network complexity. If measuring by Shannon's information, the entropy is not independent of network representation.
2. The interferences of threshold and k are measured by power-law method. 
3. [Sukhorukov et al. Model](http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1002745) is a stochastic model for mitochondrial fission-fussion process
4. Criticality is measured by [finite-size scaling](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.113.238102).








