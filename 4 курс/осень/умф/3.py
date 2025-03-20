## КР 3
import numpy as np
from scipy import integrate

# CHANGE ME
def phi(x):
  return 3.2 * np.sin(np.pi * x)**5

def psi(x):
  return -7.4 * np.sin(np.pi * x)**3
# ############################

def calc_alpha(n, l):
    func = lambda x: phi(x) * np.sin(np.pi * n * x / l)
    int_value, _ = integrate.quad(func, 0, l)
    return (2 / l) * int_value

def calc_beta(a, n, l):
    func = lambda x: psi(x) * np.sin(np.pi * n * x / l)
    int_value, _ = integrate.quad(func, 0, l)
    return (2 / (a * np.pi * n)) * int_value

def calc_omega(a, n, l): # anal
    return a * np.pi * n / l

def solve(x, t, a, N, l):
    
    series = np.ndarray(shape=(N, 1))
    for i in range(1, N+1):
        alpha = calc_alpha(n=i, l=l)
        beta = calc_beta(a=a, n=i, l=l)
        omega = calc_omega(a=a, n=i, l=l)
        series[i-1] = (alpha * np.cos(omega * t) + beta * np.sin(omega * t)) * np.sin(np.pi * i * x / l)

    return series.sum()

x = 1/3
t = 1/16
a = 4 # (корень из числа перед U''_xx(x, t))
N = 150
l = 1
print(solve(x, t, a, N, l))