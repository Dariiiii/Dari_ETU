## КР 7
import numpy as np
from scipy import integrate
from scipy.optimize import approx_fprime

# CHANGE ME
a = 6 # (корень из числа перед delta u)
l = 1 # правая граница x
m = 1 # правая граница y
x = 1/3 # U(x, ..., ...)
y = 1/3 # U(..., y, ...)
t = 1/(24*np.sqrt(2)) # U(..., ..., t)
N = 2 # количество вычисляемых членов ряда, можно не менять

def phi(x, y): # U(x, y, 0)
    return 0

def psi(x, y): # U'(x, y, 0)
    return 0

def f(x, y, t): # f(x, y, t)
    return  -1.1 * t * np.sin(np.pi * x)**3 * np.sin(np.pi * y)**3 + 9.6 * t**2 * np.sin(np.pi * x)**3 * np.sin(np.pi * y)**3
# ############################

class Solution:
    def __init__(self,
                 phi: callable,
                 psi: callable,
                 f: callable,
                 a: float,
                 l: float,
                 m: float):
        self.phi = phi
        self.psi = psi
        self.f = f
        
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
    
    def calc_b_kn(self, k, n, t):
        func = lambda y, x: self.f(x, y, t) * np.sin((np.pi * k * x)/self.l) * np.sin((np.pi * n * y)/self.m)
        int_value, _ = integrate.dblquad(func, 0, self.l, 0, self.m)
        b_kn = (4 / (self.l * self.m))  * int_value
        return b_kn
    
    def get_u0(self, x, y, t, N):
        u0 = 0
        for k in range(1, N+1):
            for n in range(1, N+1):
                a_kn = self.calc_a_kn(k=k, n=n, t=t)
                u0 += a_kn * np.sin(np.pi * k * x / self.l) * np.sin(np.pi * n * y / self.m)
        return u0
    
    def get_v(self, x, y, t, N):
        v = 0
        def calc_omega(k, n):
            g = np.pi * k / self.l
            h = np.pi * n / self.m
            return np.sqrt(self.a**2 * (g**2 + h**2))
        
        for k in range(1, N+1):
            for n in range(1, N+1):
                omega_kn = calc_omega(k, n)
                func = lambda tau: np.sin(omega_kn * (t - tau)) * self.calc_b_kn(k, n, tau)
                int_value, _ = integrate.quad(func, 0, t)
                a_kn = (1 / omega_kn) * int_value
                v += a_kn * np.sin(np.pi * k * x / self.l) * np.sin(np.pi * n * y / self.m)
        return v
    
    def solve(self, x, y, t, N):
        u0 = self.get_u0(x, y, t, N)
        v = self.get_v(x, y, t, N)
        u = u0 + v
        print(f"В поле вывода будет степень другая - не обращаем на нее внимания")
        print(f"Если вывод значения ниже такой: -1.5952728281051768e-06, ответом будет -0.15")
        print(f"Значение в точке ({x:.3f}, {y:.3f}, {t:.3f}) = {u}")
        print("Ниже самопроверка для ответа (на степень закрываем глаза =) )")
        print(f"Значение в точке ({x:.3f}, {y:.3f}, {t:.3f}) = {u * 10e4}")
        return u
    

solution = Solution(phi, psi, f, a, l, m).solve(x, y, t, N)