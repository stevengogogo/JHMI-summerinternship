# JHMI Paper Notes 20180716
:::success
:memo:**Objectives**
Today's topic is **network synchronization**. 
* Paper reading provides examples of derivation of sufficient requirements by using [Lyapunov approach](https://en.wikipedia.org/wiki/Lyapunov_stability)
* Book reading provides formal dervitation and knowledgement about synchronization in complex system.
* Talk with Dr. Brian O'Rourke about the synchronization requirement for cardial mitochondria.

---
- [ ] Paper reading
    - [ ] Synchronization of coupling oscillator
    - [ ] Cluster synchornization in networks of coupled nonidentical dynamical system
- [ ] Book reading
    - [ ] Synchronization in complex networks
- [ ] Discussion with Dr. Brian O'Rourke
    - [ ] Asking about single cell mitochondrial oscillation data
- [ ] Proposal Writing
:::

> [TOC]

## Synchronization of coupling oscillator

## Cluster synchornization in networks of coupled nonidentical dynamical system

## Synchronization in complex networks

### Definition of Synchronization

:::info
**Synchronization**

A set of coupled oscillators are said to be *synchronized* if the difference between corresponding stated become consant *asymptotically*.
:::




### Van der Pol oscillatior

$$\begin{align}
\dot{x_{i}} &= \mu (x_{i} - y_{i} - \frac{1}{3}x_{i}^{3}) \\
\dot{y_{i}} &= \frac{1}{\mu}x_{i}
\end{align}$$

### Coupled Van der Pol Oscillator

$$\begin{align}
\dot{x_{i}} &= \mu (x_{i} - y_{i} - \frac{1}{3}x_{i}^{3}) + K\sum^{N}_{p=1}(x_{p}-x_{i}) \\
\dot{y_{i}} &= \frac{1}{\mu}x_{i},
\end{align}$$

where $i, j = (1,...,N)$

### Synchronization of coupled Van der pol oscillator

* $|x_j - x_i| = \text{constant}$ as $t\rightarrow \infty \forall i,j=(1,...,N)$
    $\Rightarrow|\dot{x_j} - \dot{x_i}| = 0$
* $|y_j - y_i| = \text{constant}$ as $t\rightarrow \infty \forall i,j=(1,...,N)$
$\Rightarrow|\dot{y_j} - \dot{y_i}| = 0$

### Derivation of sufficient conditions of synchronization

### Result
:::info
**Synchronization of Van der Pol oscillator**

Couple Van der Pol oscillators sybchronize asymptotically, if coupling gain $K \geq \mu/N$
:::

## Discussion with Dr. Brian O’Rourke

:question: What are the sufficient conditions that make synchronized mitochondrial oscillation occur?
[:memo:Ref]()

:question:How to synchronize mitochondiral oscillation in single cell?
[:memo:Ref:Synchronize mitochondria network](http://www.jbc.org/content/278/45/44735)

:bulb: 

:::success
**Modulation of synchronization on mitochondrial oscillation in single cell**



:::



# Proposal Writing

## Model

### Assumptions
* Assume there a mitochondrial network poccesses $N$ mitochondria.
* For each mitochondrion

$$\dot{\phi_{i}} = f(\sum_{j=1}^{N} \phi_{j}, damaged_{i}),$$

for $j=(1,...,N)$, $damaged_{i} = \{0,1\}$

### Objective

* To find the condition that 

$$|\phi_{i} - \phi_j| = \text{constant}$$ as $t\rightarrow \infty \forall i,j = (1,...,N)$

* To find the condition that 

$$|\phi_{i} - \phi_j| = f(t)$$ 
as $t\rightarrow \infty \forall i,j = (1,...,N)$

where $\dot{f}(t) \neq 0$



## Method
