import numpy as np
from scipy import integrate
from scipy.misc import derivative

# CHANGE ME
a = 6 # (корень из числа перед U''_xx(x, t))
l = 1 # по всех условиях = 1, можно не менять
x = 1/3
t = 1/24

def f(x, t): # U''_tt(x, t) = a^2 U''_xx(x, t) + f(x, t)
    return 0

def phi(x):
  return -6.2 * np.sin(np.pi * x)**3

def psi(x):
  return np.sin(np.pi * x)**5 + 2.1

def g(t): # u(0, t)
    return 2.1 * t

def h(t): # u(l, t)
    return 2.1 * t
# ############################


class Solution:
    def __init__(self,
                 f: callable,
                 phi: callable,
                 psi: callable,
                 g: callable,
                 h: callable,
                 a: float,
                 l: float):
        # Функции
        self.f = f
        self.phi = phi
        self.psi = psi
        self.g = g
        self.h = h
        
        self.a = a
        self.l = l
    
    def calc_w(self, x, t):
        return (self.l - x) / self.l * self.g(t) + x / self.l * self.h(t)
    
    def calc_v(self, x, t, N):
        # v(x, t) = v1(x, t) + w1(x, t)
        v = self.calc_v1(x, t, N) + self.calc_w1(x, t, N)
        return v
    
    def calc_v1(self, x, t, N):        
        def calc_omega(n):
            return self.a * np.pi * n / self.l
        
        def calc_beta(n, t):
            func = lambda x: self.f(x, t) * np.sin(np.pi * n * x / l)
            int_value, _ = integrate.quad(func, 0, l)
            return (2 / l) * int_value
        
        def calc_alpha(n, t):
            omega = calc_omega(n)
            
            func = lambda tau: np.sin(omega) * (t - tau) * calc_beta(n, tau)  
            int_value, _ = integrate.quad(func, 0, t)
            return (1 / omega) * int_value
            
        v1 = 0
        for i in range(1, N+1):
            alpha = calc_alpha(n=i, t=t)
            v1 += alpha * np.sin(np.pi * i * x / self.l)
            
        return v1
    
    def calc_w1(self, x, t, N):
        w1 = 0
        
        def phi_1(x):
            return self.phi(x) - ( (self.l - x)/self.l * self.g(0) + x/self.l * self.h(0) )
        
        def psi_1(x):
            g_prime = derivative(self.g, 0, dx=1e-6)
            h_prime = derivative(self.h, 0, dx=1e-6)
            return self.psi(x) - ( (self.l - x)/self.l * g_prime + x/self.l * h_prime )
        
        def calc_alpha(n):
            func = lambda x: phi_1(x) * np.sin(np.pi * n * x / l)
            int_value, _ = integrate.quad(func, 0, l)
            return (2 / l) * int_value
        
        def calc_beta(n):
            func = lambda x: psi_1(x) * np.sin(np.pi * n * x / l)
            int_value, _ = integrate.quad(func, 0, l)
            return (2 / (a * np.pi * n)) * int_value
        
        def calc_omega(n):
            return a * np.pi * n / l
        
        for i in range(1, N+1):
            alpha = calc_alpha(n=i)
            beta = calc_beta(n=i)
            omega = calc_omega(n=i)
            w1 += (alpha * np.cos(omega * t) + beta * np.sin(omega * t)) * np.sin(np.pi * i * x / l)
            
        return w1

    
    def solve(self, x, t, N):
        # u(x, t) = v(x, t) + w(x, t)
        u = self.calc_w(x, t) + self.calc_v(x, t, N)
        
        print(f"Значение в точке ({x:.4f}, {t:.4f}) = {u}")
        return u
        
N = 100
solution = Solution(f, phi, psi, g, h, a, l).solve(x, t, N)
