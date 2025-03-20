import numpy as np
import matplotlib.pyplot as plt

def f1(x):
    return 4.225 * x**2

def f2(x):
    return 1

def f3(x):
    return 2 - 845/128 * (1 - x)**2

# Генерируем значения x для каждого интервала
x1 = np.linspace(0, 5/13, 100)
x2 = np.linspace(5/13, 9/13, 100)
x3 = np.linspace(9/13, 1, 100)

# Вычисляем соответствующие значения y для каждого интервала
y1 = f1(x1)
y2 = np.full_like(x2, f2(0))
y3 = f3(x3)

# Строим график
plt.plot(x1, y1, color='black')
plt.plot(x2, y2, color='black')
plt.plot(x3, y3, color='black')
plt.plot(0, f1(0), 'ko', markersize=8)
plt.plot(5/13, f1(5/13), 'ko', markersize=8, markerfacecolor='none')
plt.plot(5/13, f2(0), 'ko', markersize=8)
plt.plot(9/13, f2(0), 'ko', markersize=8, markerfacecolor='none')
plt.plot(9/13, f3(9/13), 'ko', markersize=8)
plt.plot(1, f3(1), 'ko', markersize=8)
plt.grid(True)

# Определение отрезков
segments = {
    '0-5/26': (0, 5/26),
    '5/26-7/13': (5/26, 7/13),
    '7/13-11/13': (7/13, 11/13),
    '11/13-1': (11/13, 1)
}

# Функция для построения графика
def plot_function(segments):
    for segment, (start, end) in segments.items():
        if segment == '0-5/26':
            x = np.linspace(start, end, 100)
            y = 3 * (x - start) / (end - start)
            plt.plot(x, y, color='red')
        elif segment == '5/26-7/13':
            x = np.linspace(start, end, 100)
            y = np.full_like(x, 3)
            plt.plot(x, y, color='red')
        elif segment == '7/13-11/13':
            x = np.linspace(start, end, 100)
            y = 3 + 2 * (x - start) / (end - start)
            plt.plot(x, y, color='red')
        elif segment == '11/13-1':
            x = np.linspace(start, end, 100)
            y = np.full_like(x, 5)
            plt.plot(x, y, color='red')

# Вызов функции для построения графика
plot_function(segments)

plt.show()
