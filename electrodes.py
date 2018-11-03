"""
electrodes.py
A module that contains various kind of input currents.
To-dos:
1. make sym2num for mutiple arguments
"""
from jitcode import t
import numpy as np
import symengine

def sigmoid(x):
    return 1./(1.+ symengine.exp(-x))

def heaviside(x):
    K = 1e3 # some big number
    return sigmoid(K*x)

def unit_pulse(t,t0,w):
    return heaviside(t-t0)*heaviside(w+t0-t)

"""
sym2num(expr):

Take an expression with symbolic object "t", like any time varying current
e.g. some_neuron.i_inj, to a normal function which is amenable to numerical
evaluation.

"""
def sym2num(t, expr):
    return symengine.Lambdify(t, expr)
