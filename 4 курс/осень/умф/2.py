## КР 2
import numpy as np
from scipy import integrate

def phi (x):
    # return -5.3 * np.abs(x) ** 5
    return 0

def psi (x):
    # return 6.2 * np.abs(x) ** 3
    return 0

def f(s, tau):
    return -1.1 * np.abs(s + tau - 9.6) ** 3

def solve (x, t, a):
    r1 = ( phi(x + a * t) + phi(x - a * t) ) / 2
    r2, _ = integrate.quad(psi, x - a * t, x + a * t)
    r3, _ = integrate.dblquad(f, 0, t, lambda tau: x - a*(t - tau), lambda tau: x + a*(t - tau))
    print(r1, r2, r3)
    return r1 + 1 / (2 * a) * r2 + 1 / (2 * a) * r3

print(solve(2, 1, 6)) # x, t, (корень из числа перед U''_xx(x, t))