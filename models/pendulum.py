import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# args = mass, gravitational acc., length of pendulum, drag coeff.
def pendulum(state, t, m, g, l, b):
    theta, omega = state
    state_deriv = [omega, -((b/m) * omega) - ((g/l) * np.sin(theta))]
    return state_deriv

# coefficients
m = 1.0
g = 9.8
l = 0.3
b = 1.0 # critical damp near 10.0

# initial condition
theta0 = np.pi/3.0
omega0 = 0.0
state0 = [theta0, omega0]

# time points
t = np.linspace(0, 5, 500)

# solve ODE
soln = odeint(pendulum, state0, t, args=(m, g, l, b))

# plot results
plt.plot(t, soln[:, 0], 'r:', label='theta(t)')
plt.plot(t, soln[:, 1], 'g-', label='omega(t)')
plt.xlabel('time')
plt.ylabel('values')
plt.grid()
plt.legend(loc='best')
plt.show()