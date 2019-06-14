import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# args = mass, drag coeff., undamped ang. freq., ext. sin force amp., ext. sin force ang. freq.
def spring(state, t, m, r, w0):
    disp, vel = state
    F0 = 0.0
    if t >= 2:
        F0 = 50.0
    state_deriv = [vel, -np.square(w0) * disp - r * vel + F0]
    return state_deriv

# coefficients
#[m,    r,                  w0,            ]
datasets = [\
[1.0,   2 * np.pi * 0.0,    2 * np.pi * 1.0], \
[1.0,   2 * np.pi * 0.7,    2 * np.pi * 1.0], \
[1.0,   2 * np.pi * 2.0,    2 * np.pi * 1.0], \
[1.0,   2 * np.pi * 3.0,    2 * np.pi * 1.0], \
[1.0,   2 * np.pi * 5.0,    2 * np.pi * 1.0], \
]

DNUM = len(datasets)

# initial condition
disp0 = 2.0
vel0 = 0.0
state0 = [disp0, vel0]

# time points
t = np.linspace(0, 10, 1000)

# solve ODE
soln = []
for i in range(0, DNUM):
    soln.append(odeint(spring, state0, t, args=tuple(datasets[i])))

# plot results
fig, axs = plt.subplots(DNUM, sharex=True, sharey=True)
fig.suptitle("Plots")

for i in range(0, DNUM):
    axs[i].plot(t, soln[i][:, 0], 'b-', label='x(t)')
    axs[i].plot(t, soln[i][:, 1], 'r:', label='v(t)')
    if i is 0:
        axs[i].legend(loc='best')    
    axs[i].grid()

fig.text(0.5, 0.04, 'time', ha='center')
fig.text(0.04, 0.5, 'values', va='center', rotation='vertical')

plt.show()
