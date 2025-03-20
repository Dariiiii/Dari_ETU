## КР 10
import numpy as np
from scipy import integrate

# CHANGE ME
a = 4 # (корень из числа перед U''_xx)
x = 1/10 # U(x, t)
t = 1/3000 # U(x, t)

def phi(x): # U(x, 0)
    return 2.1 * np.exp(-11.3 * x)
# ############################


class Solution:
    def __init__(self,
                 phi: callable,
                 a: float):
        self.phi = phi
        
        self.a = a
        
    def calc_K(self, x, t):
        return (1 / (2 * self.a * np.sqrt(np.pi * t))) * np.exp(-(x**2) / (4 * self.a**2 * t))

    def solve(self, x, t):
        y = np.linspace(-50, 50, 10000)
        dy = y[1] - y[0]
        K = self.calc_K(x - y, t)
        
        result = np.sum(self.phi(y) * K * dy)
        print(f"Ответ: {result}")
        
        ans = str(float(result))
        integer, fract = ans.split('.')
        print(f"Ответ (для копирования): {integer}.{fract[:2]}")

solution = Solution(phi, a).solve(x, t)
