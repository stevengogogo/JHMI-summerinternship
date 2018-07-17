# JHMI Paper Notes 20180712
> [time=Thu, Jul 12, 2018 9:49 AM]
> 
> [name=Shao-Ting Chiu]
> 

:::success
**Objectives**
- [x] Unvderstand redox potential 
    - [x] Ishaemia and reperfusion
    - [x] Learn how to use Sympy to solve equations
- [x] Read ROS-induced Mitochondrial membrane potential oscillation
:::

# BIOENERGETICS 4

:::success
**What I want to know?**
* Ishaemia and reperfusion
* Mitochondrial membrane potential
    * What causes $m\Delta\psi$?
        Related to oscillation
:::

## Mitochondria and cardiac ischaema/reperfusion injury

**Myocardia infarction** (heart attack) is caused by a blood clot in a *coronay artery* supplying the *left ventricle* with fuel and blood. 

* An area of ischaemia
* Glycolysis cannot adequately compensate for the failure of oxidative phosphorylation
    * intracellular acidification resulting from *lactate production* inhibits its *phosphofructokinase*.
* The *decrease* in ATP inhibits the $Na^{+}/K^{+}-ATPase$, allowing $[Ca^{2+}]_{C}$ to rise.
    * SOme concomitant AMP may be degraded, depleting the intracellular adenine nucleotide pool and gernerating [xanthine](https://www.ncbi.nlm.nih.gov/pubmed/22967988), which has been proposed to be a source of superoxide via xanthibne oxidase even under low oxygen conditions.

**Effect of ischaemic period**

|Parameter|change|
|---|---|
|$[Ca^{2+}]_{C}$|$\uparrow$|
|ATP|$\downarrow$|
|Oxidative stress|$\uparrow$|
|permeability transition|deactivated|
|Cytoplasmic pH|$\downarrow$|

**Reperfusion injury**: reperfusion can increase the damage, and there is convincing evidence for the involvement of the mitochondrial permeability transition pore (mPTP).

**The return of oxygen is the time of greatest damage to the tissue**

* return to neutral pH, further ROS production 
    * due to the combination of high $O_{2}$ and a highly reduced electron transport chain.
* Uptake into the mitochondria of $Ca^{2+}$ accumulated in the cytoplasm all contribute toward mPTP activation

* Ways to decrease reperfusion damage
    * Cyclosporin A (CsA): mPTP inhibitor
    * Ruthenium (RuRed): inhibitor of Mitochondrial Calcium Uniporter (MCU)


**Ischaemic preconditioning**
Short period of ischaemic followed by reperfusion may protect the heart against a subsequent more prolonged ischaemic attack.


:::info
[**mPTP**](https://en.wikipedia.org/wiki/Mitochondrial_permeability_transition_pore)
The mitochondrial permeability transition pore (mPTP or MPTP; also referred to as PTP, mTP or MTP) is a protein that is formed in the inner membrane of the mitochondria under certain pathological conditions such as traumatic brain injury and stroke. Opening allows increase in the permeability of the mitochondrial membranes to molecules of less than 1500 Daltons in molecular weight. Induction of the permeability transition pore, mitochondrial membrane permeability transition (mPT or MPT), can lead to mitochondrial swelling and cell death through apoptosis or necrosis depending on the particular biological setting

* Cyclosporin A (CsA) is an inhibitor of the mPTP. CsA can provide some protection against reperfusion injury
:::

# Topics of Mitochondrial Membrane Potential
### Redox potentials and the $\frac{[oxidised]}{[reduced]}$ ratio
:::warning
* Just as the standard Gibbs energy change, $\Delta G^{o}$, doesn't reflect the acutal conditions existing in the cell.

* The standard redox potential, $E^{o}$, must be qualified to take account of the relative concentrations of the oxidised and reduced species.
:::

* Actual redox potential $E$ at pH=0 for the redox couple:

    $$Oxidised + ne^{-} \leftrightarrow Reduced$$
    
    $$E = E^{o} + 2.3\frac{RT}{nF} log_{10} \frac{[oxidised]}{[reduced]}$$

* Redox potential and pH
    $$Oxidised + ne^{-} + mH^{+} \leftrightarrow Reduced$$
    
    $$E_{h,pH=x} = E_{m,pH=x} + \frac{2.3RT}{nF}log_{10}\frac{[oxidised]}{[reduced]}$$
    
#### Example of Glutathione

$$GSSG + 2H^{+} + 2e^{-} \leftrightarrow 2GSH$$

$$E_{h,pH7} = E^{o'} + \frac{RT}{2F} log_{10}\frac{[GSSH]}{[GSH]^{2}} \text{ mV}$$ 

:::success
**The pool size of glutathione is critifal for preventing oxidative stress in the mitochondria**

Proof:

1. When standard conditnon (1M GSSG and 1M GSH), at $25^{o}C$ and pH 7.0
    $$E^{o'}=-240 \text{ mV}$$
2. The total gluthaion pool concentration 
    $$[GSH] + 2[GSSH] = 10mM$$
3. Typical for the cytoplasm, a thiol redox potential of -200 mV implies a concentration of [GSSG] of 1.2mM
    $$-200 \text{ mV } = E^{o'} + 30log_{10}\frac{[GSSG]}{[10-2[GSSG]^{2}]}$$

Then
    $$[GSSG] = 1.2 mM$$
    
4. If  the pool size is lowered to 1mM, then [GSSG] must be decreased to 20 $\mu M$ to maintain the redox potential.
    * Causes problem of enzyme to reduce GSSG to GSH.
    * Explain why a maintained pool size of glutahione is critical for preventing oxidative stress in the mitochondria
:::

```python=
import matplotlib.pyplot as plt 
import numpy as np
from sympy import *

def GSSH_redox_potential(E_standard, oxidised, reduced):
    
    return E_standard + 30*(log(oxidised/reduced**2)/log(10))

# Physiological Value
gss_pool = var("GssPool")
gssh = Symbol('GSSH')
gsh = gss_pool - 2 * gssh
E_standard = -240
thio_redox = -200

print('High GSSH pool, GSSH= min',solve(GSSH_redox_potential(E_standard, gssh, 10e-3-gssh)-thio_redox
            , gssh))
print('Low GSSH pool, GSSH=',solve(GSSH_redox_potential(E_standard, gssh, 1e-3-gssh)-thio_redox
            , gssh))

# Solving the concentration of GSSH in control
exp_gsshs = solve(GSSH_redox_potential(E_standard, gssh, gsh)-thio_redox, gssh)

# Store solution
exp_gssh = exp_gsshs[0]
gsspool = np.linspace(1e-3,10e-3,100)

# Plotting seriers
f = lambdify(gss_pool, exp_gssh, "numpy")
plt.plot(gsspool, f(gsspool))
plt.ylabel('GSSH concentration (M)')
plt.xlabel('GSS Pool Concentration (M)')
plt.title('GSS pool concentration - GSSH concentration')
```
![](https://i.imgur.com/zucpaec.png)


#### Redox potential difference and the relation to $\Delta G$

$\Delta E_{h}$ clarifies that a difference between two couples, or a redox span in an elextrion transport system.

$$\Delta E_{h} = E_{h(A)} - E_{h(B)}$$

In the absence of $\Delta \phi$

$$\Delta G = -nF\Delta E_{h}$$

![](https://i.imgur.com/GUxX2M4.png =200x)

* An electron passes from N-side $\rightarrow$ P-side

$$\Delta G = -nF(\Delta E_{h} + \Delta \psi)$$

* An electron passes from P-side $\rightarrow$ N-side

$$\Delta G = -nF(\Delta E_{h}  \Delta \psi)$$

:::success
**Ion movement**

$$\Delta G = -mF\Delta \psi + 2.3RTlog_{10}\frac{[X^{m^{+}}_{B}]}{[X^{m+}_{A}]}$$

**$H^{+} movement$**

$$\Delta \mu_{H^{+}} = -F\Delta\psi + 2.3RT(pH_{Intermidiate Membrane} - pH_{Inner Membrane})$$

usually for mitochondria $pH_{Intermidiate Membrane} - pH_{Inner Membrane}<0$

**Membran potential and Goldman equation**

$$\Delta \psi = 2.3 \frac{RT}{F} log_{10} \frac{\sum P_{i}[i]_{out}}{\sum P_{i}[i]_{in}}$$
:::

---

# A Mitochondrial Oscillator Depent on Reactive Oxygen Species

## Overview

* Cell-wide synchronized oscillations in mitochondiral membrane potential ($\Delta \psi$), NADH, and ROS production have been recently described in isolated cardiomyocytes.
* Superoxide anion efflux through inner membrane anion channels and the intracellular ROS scavenging capacity play a key role in the oscillatory mechanism.
* Methodology
    * Computational model of mitochondrial energetifs and $Ca^{2+}$ handling including mitochondrial ROS production, cytoplasmic ROS scavenging, and ROS activation of inner membrane anion flux.

* Spontaneous metabolic oscillations in substrate-deprived cardiac myocytes that were shown to deive oscillations in [sacrolemal](https://en.wikipedia.org/wiki/Sarcolemma) $K^{+}$ currents 
* An invesitgation of the subcellular sptiotemporal patterns of this phenomenon revealed heterogeneous mitochondrial polarization and propagated mitochondrial redox waves.
* the oscillatory depolarizations of $\Delta \psi_{m}$ **did not** involve the classical permeability transition pore or dependd on intracellular $Ca^{2+}$, underscoring the unique features of the mitochondrial oscillator in the intact myocyte.
* Oscillaton due to interplay between mitochondrial ROS production and ROS scavenging systems of the cell.

## Modeling Superoxide Production in the Respiratory Chain

* The redox potential of the site of ROS production by Complex I was estimated to be -392mV, which is 72mV more negative than the NADH/NAD redox couple itself. 
    * ROS production from this thermodynamically unfavorable state is usually promoted by inhibiting respiration.

:::success
* What is the necessary requirements of the mathematical model to behave as biological oscillator
    * parameter screening
* it looks like a square wave oscillator with very high duty cycle
* How were those scavenger models generated? based on mass-equation or Nerst equation
:::














