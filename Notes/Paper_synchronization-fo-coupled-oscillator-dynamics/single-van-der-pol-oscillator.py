#%% Van-der-Pol-oscillator
import numpy as np
from scipy.integrate import odeint

def single_van_oscillator(var, t, mu):
    x,y = var
    dfdt = [
        mu * (x-y-(1/3) * x**3),
        (1/mu)*x
    ]
    return dfdt
# Parameters
x0, y0 = -1, 2
mu = 1

# Pack up
var0 = [x0, y0]

# Solve the differential equation

## ODE solver parameters
stoptime = 50.0
numpoints = 1000

# Create the time samples for the output of the ODE solver.
t = np.linspace(0, stoptime, numpoints)

# Call the ODE solver 
wsol = odeint(single_van_oscillator, var0, t, args=(mu,))





#Plot
import matplotlib.pyplot as plt 
fig_reaction = plt.figure()

plt.plot(t,wsol[:,0])

plt.legend()
plt.grid()
plt.title('Single Van der Pol Oscillator')
plt.xlabel('time')
plt.ylabel('Amplitute')
plt.savefig('SIMULATION_single-van-der-pol.png')
plt.show()

