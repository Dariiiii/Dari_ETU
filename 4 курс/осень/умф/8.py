## КР 8
import numpy as np
from scipy import integrate
import sympy as sp

# CHANGE ME
a = 6 # (корень из числа перед U''_xx)
l = 1 # правая граница x
x = 1/6 # U(x, t)

def phi(x): # U(x, 0)
    return 2.1 * np.sin(np.pi * x)**3 - 8.7 * np.sin(np.pi * x)
# ############################


N = 1 # НЕ МЕНЯТЬ!!!
class Solution:
    def __init__(self,
                 phi: callable,
                 a: float,
                 l: float,
                 N: int):
        self.phi = phi
        
        self.a = a
        self.l = l
        self.N = N
        
    def calc_u(self, x, t):
        u = 0
        def calc_an(n):
            wn = (self.a * np.pi * n) / self.l
            
            int_func = lambda x: self.phi(x) * np.sin(np.pi * n * x / self.l)
            int_value, _ = integrate.quad(int_func, 0, self.l)
            alpha_n = (2 / self.l) * int_value
            
            return alpha_n * sp.exp(-1 * wn**2 * t)
        
        for n in range(1, self.N+1):
            an = calc_an(n)
            u += an * np.sin(np.pi * n * x / self.l)
        return u

    def solve(self, x):
        t = sp.symbols('t')
        u_xt = self.calc_u(x, t)
        biba = sp.exp(self.a**2 * np.pi**2 * t)
        print(f"Значение экспоненты перед U =", biba)
        print(f"Значение U({x:.3f}, t) =", u_xt)
        
        f = u_xt * biba
        
        lim_value = sp.limit(f, t, sp.oo)
        print(f"Значение предела (ответ):", float(lim_value))
        
        ans = str(float(lim_value))
        integer, fract = ans.split('.')
        print(f"Первые два знака ответа (ответ для копирования): {integer}.{fract[:2]}" )
        print("ATTENTION: если в ответе будет ответ по типу 3.14999999, НЕ ОКРУГЛЯТЬ!!!!")
    

solution = Solution(phi, a, l, N).solve(x)
