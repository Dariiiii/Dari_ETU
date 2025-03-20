## КР 6
import numpy as np
from scipy import integrate

# CHANGE ME
a = 8 # (корень из числа перед delta u)
l = 1 # правая граница x
m = 1 # правая граница y
x = 1/3
y = 1/3
t = 1/(32*np.sqrt(2))
N = 20 # количество вычисляемых членов ряда, можно не менять

def phi(x, y): # U(x, y, 0)
  return 2.1 * np.sin(np.pi * x)**3 * np.sin(np.pi * y)**3

def psi(x, y): # U'(x, y, 0)
  return 9.6 * np.sin(np.pi * x)**3 * np.sin(np.pi * y)**3
# ############################

class Solution:
    def __init__(self,
                 phi: callable,
                 psi: callable,
                 a: float,
                 l: float,
                 m: float):
        self.phi = phi
        self.psi = psi
        
        self.a = a
        self.l = l
        self.m = m
        
    def calc_a_kn(self, k, n, t):
        def calc_alpha():
            func = lambda y, x: self.phi(x, y) * np.sin(np.pi * k * x / self.l) * np.sin(np.pi * n * y / self.m)
            int_value, _ = integrate.dblquad(func, 0, self.l, 0, self.m)
            return (4 / (self.l * self.m)) * int_value
        
        def calc_omega():
            g = np.pi * k / self.l
            h = np.pi * n / self.m
            return np.sqrt(self.a**2 * (g**2 + h**2))
        
        def calc_beta():
            func = lambda y, x: self.psi(x, y) * np.sin(np.pi * k * x / self.l) * np.sin(np.pi * n * y / self.m)
            int_value, _ = integrate.dblquad(func, 0, self.l, 0, self.m)
            omega = calc_omega()
            return (4 / (self.l * self.m * omega)) * int_value
        
        omega = calc_omega()
        alpha = calc_alpha()
        beta = calc_beta()
        a_kn = alpha * np.cos(omega * t) + beta * np.sin(omega * t)
        
        return a_kn

    
    def solve(self, x, y, t, N):
        u = 0
        for k in range(1, N+1):
            for n in range(1, N+1):
                a_kn = self.calc_a_kn(k=k, n=n, t=t)
                u += a_kn * np.sin(np.pi * k * x / self.l) * np.sin(np.pi * n * y / self.l)

        print(f"Значение в точке ({x:.3f}, {y:.3f}, {t:.3f}) = {u}")
        return u
    

solution = Solution(phi, psi, a, l, m).solve(x, y, t, N)
