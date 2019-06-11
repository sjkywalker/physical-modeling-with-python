import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# function that returns dx/dt, dy/dt
def xmodel(x, t):
    dxdt = 3.0 * np.exp(-t)
    return dxdt

def ymodel(y, t):
    dydt = 3 - y
    return dydt

# initial condition
x0 = 0
y0 = 0

# time points
t = np.linspace(0, 5)

# solve ODE
x = odeint(xmodel, x0, t)
y = odeint(ymodel, y0, t)

# plot results
plt.plot(t, x, 'b-', label=r'$\frac{dx}{dt}=3 \; \exp(-t)$')
plt.plot(t, y, 'r--', label=r'$\frac{dy}{dt}=-y+3$')
plt.xlabel('time')
plt.ylabel('response')
plt.legend(loc='best')
plt.show()
