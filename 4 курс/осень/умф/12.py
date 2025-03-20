## КР 12
import numpy as np
from scipy.integrate import quad

# CHANGE ME
R = 6 # при x^2 + y^2 = R^2
x = 0 # U(x, y) \
      #           = N 
y = 0 # U(x, y) /


def phi(x, y): # Граничное условие U(x, y)
    return -2.1 * np.abs(x) + 8.7 * y**2
# ############################


class Solution:
    def __init__(self,
                 phi: callable,
                 R: float):
        self.phi = phi
        
        self.R = R
        
    def dist_square(self, x, y, x0, y0):
        return (x0 - x)**2 + (y0 - y)**2

    def solve(self, x, y):
        def integrand(t):
            # Точка M
            x0 = self.R * np.cos(t)
            y0 = self.R * np.sin(t)
            return (self.R**2 - self.dist_square(0, 0, x, y)) / (self.R * self.dist_square(x0, y0, x, y)) * phi(x0, y0)

        # Вычисление интеграла
        result, _ = quad(integrand, 0, 2 * np.pi)
        result = 1 / (2 * np.pi) * result
        print(result)
        
        ans = str(float(result))
        integer, fract = ans.split('.')
        print(f"Ответ (для копирования): {integer}.{fract[:2]}")

solution = Solution(phi, R).solve(x, y)
