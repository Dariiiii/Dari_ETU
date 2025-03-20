import numpy as np
from scipy.stats import f

# Данные по износостойкости деталей (тыс. час)
p = 3  # Количество групп (материалов)
q = 5  # Количество наблюдений в каждой группе
material_1 = np.array([1.25, 1.32, 1.28, 1.26, 1.29])
material_2 = np.array([1.12, 1.15, 1.26, 1.19, 1.21])
material_3 = np.array([1.32, 1.33, 1.34, 1.29, 1.30])
full_material = np.array([material_1, material_2, material_3])

# Вычисление константы
mean_full_material = np.mean(full_material)
print(f"Среднее для всех материалов: {mean_full_material:.3f}")

# Центрирование данных
material_1_centered = material_1 - mean_full_material
material_2_centered = material_2 - mean_full_material
material_3_centered = material_3 - mean_full_material

# Вычисление Q_j (сумма квадратов для каждой группы)
Q1 = np.sum(material_1_centered ** 2)
Q2 = np.sum(material_2_centered ** 2)
Q3 = np.sum(material_3_centered ** 2)
print(f"Q_j: {[round(Q1, 3), round(Q2, 3), round(Q3, 3)]}")

# Вычисление T_j (сумма для каждой группы)
T1 = np.sum(material_1_centered)
T2 = np.sum(material_2_centered)
T3 = np.sum(material_3_centered)
print(f"T_j: {[round(T1, 3), round(T2, 3), round(T3, 3)]}")

# Сумма Q_j и T_j
sum_Q = Q1 + Q2 + Q3
sum_T = T1 + T2 + T3
print(f"Сумма Q_j: {round(sum_Q, 3)}")
print(f"Сумма T_j: {round(sum_T, 3)}")

# Вычисление T_j^2
T1_squared = T1 ** 2
T2_squared = T2 ** 2
T3_squared = T3 ** 2
print(f"T_j^2: {[round(T1_squared, 3), round(T2_squared, 3), round(T3_squared, 3)]}")

# Сумма T_j^2
sum_T2 = T1_squared + T2_squared + T3_squared
print(f"Сумма T_j^2: {round(sum_T2, 3)}")

# Вычисление сумм квадратов
S_obch = sum_Q - sum_T ** 2 / (p * q)
S_fact = sum_T2 / q - sum_T ** 2 / (p * q)
print(f"S_общ: {round(S_obch, 3)}")
print(f"S_факт: {round(S_fact, 3)}")

# Остаточная сумма квадратов
S_ost = S_obch - S_fact
print(f"S_ост: {round(S_ost, 3)}")

# Дисперсии
s2_obch = S_obch / (p * q - 1)
s2_fact = S_fact / (p - 1)
s2_ost = S_ost / (p * (q - 1))
print(f"s2_общ: {round(s2_obch, 3)}")
print(f"s2_факт: {round(s2_fact, 3)}")
print(f"s2_ост: {round(s2_ost, 3)}")

# Критерий Фишера
F = s2_fact / s2_ost
print(f"F-критерий: {round(F, 3)}")

# Коэффициент детерминации
eta2 = S_fact / S_obch
print(f"Коэффициент детерминации (η^2): {round(eta2, 3)}")

# Критическое значение F-распределения
alpha = 0.05
F_critical = f.ppf(1 - alpha, p - 1, p * (q - 1))
print(f"Критическое значение F-распределения: {round(F_critical, 3)}")

# Проверка гипотезы
if F > F_critical:
    print("Нулевая гипотеза отвергается. Материал влияет на износостойкость.")
else:
    print("Нулевая гипотеза не отвергается. Материал не влияет на износостойкость.")