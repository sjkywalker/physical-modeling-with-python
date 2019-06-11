import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# function that returns dy/dt
def model(y, t):
    u = 0
    if t >= 10:
        u = 2
    
    dydt = (float(1)/5) * (-y + u)
    return dydt

# initial condition
y0 = 1

# time points
t = np.linspace(0, 40, 1000)

# solve ODE
y = odeint(model, y0, t)

# plot results
plt.plot(t, y, 'r-', label='Output (y(t))')
plt.plot([0, 10, 10, 40], [0, 0, 2, 2], 'b-', label='Input (u(t))')
plt.xlabel('time')
plt.ylabel('values')
plt.legend(loc='best')
plt.show()
