 
# JHMI Paper Notes 20180716-17

:memo:**Objectives**
Today's topic is **network synchronization**. 
* Paper reading provides examples of derivation of sufficient requirements by using [Lyapunov approach](https://en.wikipedia.org/wiki/Lyapunov_stability)
* Book reading provides formal dervitation and knowledgement about synchronization in complex system.
* Talk with Dr. Brian O'Rourke about the synchronization requirement for cardial mitochondria.

---
- [ ] Paper reading
    - [x] Synchronization of coupling oscillator
    - [ ] Cluster synchornization in networks of coupled nonidentical dynamical system
- [ ] Book reading
    - [ ] Synchronization in complex networks
- [x] Discussion with Dr. Brian O'Rourke
    - [x] Asking about single cell mitochondrial oscillation data
- [ ] Proposal Writing

---


[TOC]




# Cluster synchornization in networks of coupled nonidentical dynamical system

:memo: **Objectives**
* Study cluster synchronization in networks of coupled nonidentical dynamical systems
* Find two essential conditions for unweighted graph topology to realize cluster synchronization
    *  Common intercluster coupling condition
    * Intracluster communication
* Two manners of weighting to achieve cluster synchronization.
    * Adding positive weights on each edge with keeping ther invariance of the cluster synchronization manifold
    * Adaptive feedback weighting algorithm

|Cluster synchronization method|Description|
|---|---|
|Self-organization|cluster with dominant intracluster coupling|
|Driving|leads to cluster with dominant intercluster couplings|

## Notation and Formulation

### Matrix

:book:**Positive matrix**
a matrix $Z$ is positive definite on a linear subspace $V$ if $u^{T}Zu\gt 0 $
for all $u\in V$ and $u \neq 0$, denoted by $Z|_{V} \gt 0$

:book: **$\lambda_{k}(Z)$**
If a matrix $Z$ has all eigenvalues real, then $\lambda_{k}(Z)$ the $k^{\text{th}}$ largest eigenvalues of $Z$

:book: **$Z^{s} = (Z + Z^{T})/2$**

### Graph

:book: **Bidirected unweighted graph**

* $G$ is denoted by a double set $\{V,E\}$, 
* where $V$ is the vertex set numbered by $\{1,...,m\}$
* $E$ denotes the edge set with $e(i,j)\in E$ if and only if there is an edge connecting vertices $j$ and $i$
* $N(i)=\{j \in V:e(i,j) \in E\}$
    denotes the neighborhood set of vertex $i$

:book:**Cluster** 
A cluster $C$ is a disjoint division of the vertex set 

$$V: C=\{C_{1},C_{2},...,C_{K}\}$$

satisfying

* $\cup_{k=1}^{K} C_{k} = V$
* $C_{k} \cap C_{l} = 0$ 
    holds for $k \neq l$

### System on a vertex

The individual uncoupled system on the vertex $i$ is denoted by an n-dimensional ordinary differential equation,

$$\dot{\vec{x}}^{i} = f_{k}(\vec{x}^{i})$$

for $i\in C_{k}$, where 

$$\vec{x}^{i} = [x^{i}_{1},...,x^{i}_{n}]^{T}$$

is the state varible vector vector on vertex $i$ and $f_{k}(\cdot):R^{n}\rightarrow R^{n}$ is continuous vector-valued function.

:bulb: Each vertex in the same cluster has the same individual node dynamics

:bulb: $f_{k}$ for different clusters are distinct

### Example of Linearly coupled dynamical system

$$\dot{x}^{i} = f_{k}(x^{i}) + \sum_{j\in N(i)}w_{ij}\Gamma(x^{j}-x^{i})$$


where $i\in C_{k}$, $k=1,...,K$,
* $w_{ij}$ is the coupling weight at the edge from vertex $j$ to $i$
* $\Gamma = [\gamma_{uv}]^{n}_{u,v=1}$
    denotes the inner connection by the way that $\gamma_{uv} \neq 0$ if the u$^{\text{th}}$ of the vertices can be influeced by the v$^{\text{th}}$ component.


# Synchronization in complex networks

# Synchronization of Coupling Oscillator Dynamics

## Objectives

* Derive sufficient conditions for sunchronization of selected benchmark oscillators which are linearly coupled.
* Use Lyapunov approach to obtain sufficiency condition for synchronization of coupled oscillators.
* Study synchronization of Van der Pol oscillators and Fitzhugh Nagumo oscillators with all-to-all connectivity.

## Definition of Synchronization

:bulb:**Synchronization**

A set of coupled oscillators are said to be *synchronized* if the difference between corresponding stated become consant *asymptotically*.


## Kuramoto Coupled Oscillator

$$
\dot{\theta_{i}} = \omega_{i} + \frac{K}{n}\sum^{n}_{j=1} sin(\theta_{j} - \theta_{i})
$$

$i \in 1,...,n$

where, $\theta_{i}$ is phase, $\omega_{i}$ is natural frequency and K is coupling gain of the oscillator

@import "SIMULATION_kuramoto-oscillator.png"
@import "kuramoto-model.py"



## Van der Pol oscillatior

[Van der Pol oscillator](https://en.wikipedia.org/wiki/Van_der_Pol_oscillator) is a non-conservative oscillator with non-linear damping. 

$\frac{d^{2}x}{dt^{2}} - \mu(1-x^{2})\frac{dx}{dt} + x = 0$

The equation can be rewritten to the following system with $y = x - x^{3}/3 - \dot{x}/\mu$

### Single Van der Pol Oscillator

$$\begin{aligned}
\dot{x_{i}} &= \mu (x_{i} - y_{i} - \frac{1}{3}x_{i}^{3}) \\
\dot{y_{i}} &= \frac{1}{\mu}x_{i}
\end{aligned}$$

@import "SIMULATION_single-van-der-pol.png"
@import "single-van-der-pol-oscillator.py"

### Coupled Van der Pol Oscillator

$$\begin{aligned}
\dot{x_{i}} &= \mu (x_{i} - y_{i} - \frac{1}{3}x_{i}^{3}) + K\sum^{N}_{p=1}(x_{p}-x_{i}) \\
\dot{y_{i}} &= \frac{1}{\mu}x_{i},
\end{aligned}$$

where $i, j = (1,...,N)$

### Synchronization of coupled Van der pol oscillator


* $|x_j - x_i| = \text{constant}$ as $t\rightarrow \infty \forall i,j=(1,...,N)$
    $\Rightarrow|\dot{x_j} - \dot{x_i}| = 0$
* $|y_j - y_i| = \text{constant}$ as $t\rightarrow \infty \forall i,j=(1,...,N)$
$\Rightarrow|\dot{y_j} - \dot{y_i}| = 0$

### The difference dynamics of Van der Pol oscillators

![Screen Shot 2018-07-17 at 4.19.49 PM](https://i.imgur.com/4zIM1Tg.png)

### Derivation of sufficient conditions of synchronization

#### Theorem 1
Consider system dymamics of coupled Van der Pol oscillator. Let at t=0, $(x_{i}, x_{j}, y_{i}, y_{j})\in R$
$\forall i,j = (1,...,N)$
Then early coupled Van der Pol oscillators synchronize asymptotcially, if coupling gain $K \geq \mu/N$

**Proof:**

Let the positive definite Lyapunov function $S_{ij}$ be given as,

$S_{ij} = \frac{1}{2}(x_{j}-x_{i})^{2}$

![Screen Shot 2018-07-17 at 4.27.36 PM](https://i.imgur.com/KcFbEJ3.png)

Let the positive definite Lyapynov function $P_{ij}
$ be given as,

$P_{ij} = \frac{1}{2}(y_{j}-y_{i})^{2}$

![Screen Shot 2018-07-17 at 4.31.42 PM](https://i.imgur.com/lX6tviN.png)

$L_{ij} = S_{ij} + (\mu)^{2}P_{ij}$

![Screen Shot 2018-07-17 at 4.35.17 PM](https://i.imgur.com/QZl9Wx8.png)


### Conclusion

**Synchronization of Van der Pol oscillator**

Couple Van der Pol oscillators sybchronize asymptotically, if coupling gain $K \geq \mu/N$

The Lyapunov approach based conditionon  sufficient coupling gain for synchronization of linearly coupled Van der Pol oscillator and linearly coupled Fitzhugh  Nagumo neural oscillators using theorem 1 have been derived.




# Discussion with Dr. Brian O’Rourke

## Questions

:question: What are the sufficient conditions that make synchronized mitochondrial oscillation occur?

* In normal physiology status, mitochodnrial $\Delta\psi_{m}$ are oscillating asynchronizedly
* When Cell is under stress in partially mitochondiral network or all of it. The mitochondrial network will somehow oscillate synchronizedly. 

:question:How to synchronize mitochondiral oscillation in single cell?
[:memo:Ref:Synchronize mitochondria network](http://www.jbc.org/content/278/45/44735)

* By stress

## Brian's Experiment: The propagation of mitochondrial damage

:memo: **Objectives**
* To see whether mitochondria are connected electrically.
* To know how partially damage of mitochondria influences the overall mitochondrial network

## Experiment Design

1. Tranfection of Rhodopsin
2. Two photon microscopy imaging

# Proposal Writing

## Model

## Assumptions
* Assume there a mitochondrial network poccesses $N$ mitochondria.
* For each mitochondrion

$$\dot{\phi_{i}} = f(\sum_{j=1}^{N} \phi_{j}, damaged_{i}),$$

for $j=(1,...,N)$, $damaged_{i} = \{0,1\}$

## Objective

* To find the condition that 

$$|\phi_{i} - \phi_j| = \text{constant}$$ as $t\rightarrow \infty \forall i,j = (1,...,N)$

* To find the condition that 

$$|\phi_{i} - \phi_j| = f(t)$$ 
as $t\rightarrow \infty \forall i,j = (1,...,N)$

where $\dot{f}(t) \neq 0$ as $t\rightarrow \infty$



## Method

Lyquanov method?
