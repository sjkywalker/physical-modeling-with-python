# Physical Modeling with Python

Simulate physical models with python ODEINT

## Environment

### OS

Ubuntu 16.04 LTS Xenial Xerus

### Python with VS Code

venv=2.7

### Modules

numpy==1.16.4

scipy==1.2.2

matplotlib==2.2.4

## Overview

A physical system simulator with python. Main objective is to get the right answers by solving ordinary differential equations, using the `odeint` function.

## Structure

### `./examples/` directory

Contains tutorial codes from [here](https://apmonitor.com/pdc/index.php/Main/SolveDifferentialEquations). Custom code may be different from original. It is a great source to practice modeling.

### `./models/` directory

Contains acutal implementations of a simple pendulum and a spring pendulum. Also added custom models with external force.

* No Force (Constant)
* Step Function
* Sinusoidal
* Exponential

There's also a `main.py` file which represents these models - it's based on the sinusoidal force model.

## Acknowledgement

* [Solve Differential Equations with ODEINT](https://apmonitor.com/pdc/index.php/Main/SolveDifferentialEquations)
