import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# args = mass, spring coeff., drag coeff.
def spring(state, t, m, k, b):
    disp, vel = state
    state_deriv = [vel, -(k/m) * disp - (b/m) * vel]
    return state_deriv

# coefficients
m = 2.0
k = 100.0
b = 5.0 # critical damp near 25.0

# initial condition
disp0 = 0.5
vel0 = 0.0
state0 = [disp0, vel0]

# time points
t = np.linspace(0, 5, 500)

# solve ODE
soln = odeint(spring, state0, t, args=(m, k, b))

# plot results
plt.plot(t, soln[:, 0], 'r:', label='x(t)')
plt.plot(t, soln[:, 1], 'g-', label='v(t)')
plt.xlabel('time')
plt.ylabel('values')
plt.grid()
plt.show()
