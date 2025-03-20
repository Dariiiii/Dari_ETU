import numpy as np
import matplotlib.pyplot as plt

def calculate_probabilities(P, Q, steps, current_step=1):
    P_B = sum(P[i] * Q[i] for i in range(len(P)))
    P_new = [P[i] * Q[i] / P_B for i in range(len(P))]
    for i, prob in enumerate(P_new):
        if i == 0:
            P_A1.append(prob)
        elif i == 1:
            P_A2.append(prob)
        elif i == 2:
            P_A3.append(prob)
    if current_step == steps:
        return P_new
    return calculate_probabilities(P_new, Q, steps, current_step + 1)

def plot_probabilities(x, P_A1, P_A2, P_A3):
    plt.figure(figsize=(10, 6))
    plt.plot(x, P_A1, marker='o', label='Завод 1', color='blue')
    plt.plot(x, P_A2, marker='o', label='Завод 2', color='red')
    plt.plot(x, P_A3, marker='o', label='Завод 3', color='green')
    plt.xticks(x)
    plt.xlabel('Шаг')
    plt.ylabel('Вероятность')
    plt.title('Вероятности для каждого завода на каждом шаге')
    plt.legend()
    plt.grid(True)
    plt.show()

def approximate_with_polynomial(x, y, degree):
    coefficients = np.polyfit(x, y, degree)
    polynomial = np.poly1d(coefficients)
    coeff_str = ", ".join([f"{coeff:.4f}" for coeff in coefficients])
    legend_label = f"Полином степени {degree}\nКоэффициенты: [{coeff_str}]"
    y_approx = polynomial(x)
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, color='blue', label='Исходные данные (P)')
    plt.plot(x, y_approx, color='red', label=legend_label)
    plt.xticks(x)
    plt.xlabel('Шаг')
    plt.ylabel('Вероятность')
    plt.title(f'Аппроксимация полиномом степени {degree}')
    plt.legend()
    plt.grid(True)
    plt.show()
    return coefficients

def plot_polynomial_with_points(x, y, coefficients):
    polynomial = np.poly1d(coefficients)
    y_approx = polynomial(x)
    for i in range(len(x)):
        if abs(y[i] - y_approx[i]) > 0.01:
            print(f"Отклонение > 0.01 на шаге {i + 1}")
            break
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, color='blue', label='Исходные данные (точки)')
    plt.plot(x, y_approx, color='red', label=f'Полином: {polynomial}')
    plt.xticks(x)
    plt.xlabel('Шаг')
    plt.ylabel('Вероятность')
    plt.title('Полином и исходные данные')
    plt.legend()
    plt.grid(True)
    plt.show()

P = [2 / 11, 4 / 11, 5 / 11]
Q = [0.94, 0.96, 0.93]
steps = 20
P_A1 = []
P_A2 = []
P_A3 = []

result = calculate_probabilities(P, Q, steps)

x = np.arange(1, steps + 1)
y = np.array(P_A2)
degree = 2

coefficients = approximate_with_polynomial(x, y, degree)
print(f"Коэффициенты полинома степени {degree}: {coefficients}")

P_A2 = []
steps = 70
result = calculate_probabilities(P, Q, steps)
x = np.arange(1, steps + 1)
y = np.array(P_A2)

plot_polynomial_with_points(x, y, coefficients)