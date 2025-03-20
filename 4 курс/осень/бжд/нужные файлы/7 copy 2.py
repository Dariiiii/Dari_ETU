import matplotlib.pyplot as plt
import numpy as np

# Частоты и значения звукоизоляции
frequencies = [63, 125, 250, 500, 1000, 2000, 4000, 8000]
rdb = [30, 40, 50, 60, 70]  # Значения звукоизоляции для первых пяти частот

# Добавим значения для всех частот, чтобы длины массивов совпадали
rdb += [70, 70, 70]  # Добавим значения для оставшихся частот

# Добавим значения для 1/3 октавы
third_octave_frequencies = [
    50, 80, 100, 160, 200, 315, 400, 630, 800, 1250, 1600, 2500, 3150, 5000, 6300
]
third_octave_rdb = [
    25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95
]

# Объединим частоты и значения звукоизоляции
all_frequencies = sorted(frequencies + third_octave_frequencies)
all_rdb = []

# Создаем словарь для сопоставления частот и значений звукоизоляции
frequency_rdb_map = {freq: rdb for freq, rdb in zip(frequencies, rdb)}
frequency_rdb_map.update({freq: rdb for freq, rdb in zip(third_octave_frequencies, third_octave_rdb)})

# Заполняем значения звукоизоляции для всех частот
for freq in all_frequencies:
    all_rdb.append(frequency_rdb_map[freq])

# Координаты точек B и C
B = (315, 33)
C = (315, 65)

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(all_frequencies, all_rdb, marker='o', label='Звукоизоляция')

# Горизонтальный отрезок ВА
plt.hlines(y=B[1], xmin=all_frequencies[0], xmax=B[0], colors='r', linestyles='dashed')

# Отрезок ВС с наклоном 6 дБ на октаву
slope = 6 / (np.log2(2 * B[0]) - np.log2(B[0]))
x_values = np.linspace(B[0], 8000, 100)
y_values = B[1] + slope * (np.log2(x_values) - np.log2(B[0]))
plt.plot(x_values, y_values, color='r', linestyle='dashed')

# Точки B и C
plt.plot(B[0], B[1], 'ro')
plt.plot(C[0], C[1], 'ro')

# Подписи
plt.text(B[0], B[1], 'B', verticalalignment='bottom', horizontalalignment='right')
plt.text(C[0], C[1], 'C', verticalalignment='bottom', horizontalalignment='right')

# Настройка графика
plt.xscale('log')
plt.xlabel('Частота (Гц)')
plt.ylabel('Звукоизоляция (дБ)')
plt.title('Частотная характеристика звукоизоляции сплошной бетонной перегородки толщиной 0,12 м')
plt.grid(True)
plt.legend()
plt.show()
