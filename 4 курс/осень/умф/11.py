import numpy as np
from scipy import integrate

# Параметры задачи
a = 7  # sqrt(49)
x = 1 / 10
t = 1 / 3000
f = lambda x: 3.2 * np.exp(9.6 * x)  # Неоднородная часть уравнения


class Solution:
    def __init__(self, a: float, f: callable):
        self.a = a
        self.f = f

    def calc_K(self, x, t):
        if t <= 0:
            return np.zeros_like(x)
        return (1 / np.sqrt(4 * self.a ** 2 * np.pi * t)) * np.exp(-(x ** 2) / (4 * self.a ** 2 * t))

    def solve(self, x, t):
        # Уменьшаем диапазон интегрирования и увеличиваем плотность точек
        y = np.linspace(-10, 10, 5000)
        tau = np.linspace(1e-10, t, 5000)
        dy = y[1] - y[0]
        dtau = tau[1] - tau[0]

        result = 0

        for current_tau in tau:
            try:
                K = self.calc_K(x - y, t - current_tau)
                f_values = self.f(y)
                result += np.nansum(f_values * K) * dy * dtau
            except:
                continue


        print(f"Ответ: {result}")


solution = Solution(a, f).solve(x, t)
