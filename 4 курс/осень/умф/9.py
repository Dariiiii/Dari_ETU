## КР 9
import numpy as np
from scipy import integrate

# CHANGE ME
a = 7 # (корень из числа перед U''_xx)
l = 1 # правая граница x
x = 1/6 # U(x, t)
t = 1 # U(x, t)

def phi(x): # U(x, 0)
    return 0

def f(x, t):
    return t * (-1.1 * np.sin(np.pi * x)**3 - 9.6 * np.sin(np.pi * x))
# ############################


N = 100 # НЕ МЕНЯТЬ!!!
class Solution:
    def __init__(self,
                 phi: callable,
                 f: callable,
                 a: float,
                 l: float,
                 N: int):
        self.phi = phi
        self.f = f
        
        self.a = a
        self.l = l
        self.N = N
        
    def calc_u(self, x, t):
        u = 0
        
        def calc_an(n):
            wn = (self.a * np.pi * n) / self.l
            
            def calc_betan(tau, n):
                int_func = lambda xi: self.f(xi, tau) * np.sin(n * np.pi * xi / self.l)
                int_value, _ = integrate.quad(int_func, 0, self.l)
                return (2 / self.l) * int_value
            
            # Вычисление первого аргумента alpha_n(0) e^{-wn^2 t}
            int_func = lambda x: self.phi(x) * np.sin(np.pi * n * x / self.l)
            int_value, _ = integrate.quad(int_func, 0, self.l)
            alpha_n_init = (2 / self.l) * int_value
            alpha_n =  alpha_n_init * np.exp(-1 * wn**2 * t)
            
            # Вычисление второго аргумента e^{-wn^2 t} \int_0^t e * beta(t) dt
            int_func = lambda tau: np.exp(-1 * wn**2 * (t - tau)) * calc_betan(tau, n)
            int_value, _ = integrate.quad(int_func, 0, t)
            beta_n = int_value
            
            return alpha_n + beta_n
        
        for n in range(1, self.N+1):
            an = calc_an(n)
            u += an * np.sin(np.pi * n * x / self.l)
        return u

    def solve(self, x, t):
        u = self.calc_u(x, t)
        
        print(f"Ответ: {u * 1e4}")
        ans = str(float(u * 1e4))
        integer, fract = ans.split('.')
        print(f"Ответ (для копирования): {integer}.{fract[:2]}")
        

solution = Solution(phi, f, a, l, N).solve(x, t)
