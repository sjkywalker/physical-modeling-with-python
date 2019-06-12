import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# args = mass, drag coeff., undamped ang. freq., ext. sin force amp., ext. sin force ang. freq.
def spring(state, t, m, r, w0, F0, w):
    disp, vel = state
    state_deriv = [vel, -np.square(w0) * disp - r * vel + (F0/m) * np.sin(w*t)]
    return state_deriv

# coefficients
m = 2.0
r = 1.0 #2 * np.pi * 2.0 #1.0
w0 = 2 * np.pi * 1.0
F0 = 10.0 #10.0
w = 2 * np.pi * 0.5

# initial condition
disp0 = 0.5
vel0 = 0.0
state0 = [disp0, vel0]

# time points
t = np.linspace(0, 5, 500)

# solve ODE
soln = odeint(spring, state0, t, args=(m, r, w0, F0, w))

# plot results
plt.plot(t, soln[:, 0], 'r:', label='x(t)')
plt.plot(t, soln[:, 1], 'g-', label='v(t)')
plt.xlabel('time')
plt.ylabel('values')
plt.grid()
plt.show()
