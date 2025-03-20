import matplotlib.pyplot as plt
import time

# Частоты и уровни звукового давления
frequencies = [31.5, 63, 125, 250, 500, 1000, 2000, 4000, 8000]
background_noise = [62.4, 60.5, 44, 48.8, 43, 30, 26.5, 20.2, 16.4]
noise_source_unprotected = [58.8, 66, 59.4, 80.8, 88.3, 99, 100.5, 91.6, 67.8]
noise_source_in_shell_1 = [60.5, 66.6, 53.2, 66.9, 82.7, 96.1, 92.5, 84.3, 52.1]
noise_source_in_shell_2 = [64, 65.5, 57.6, 67.5, 81.4, 85.2, 81.5, 70.5, 38.3]
noise_source_with_screen_1 = [64.8, 66.1, 58, 76.8, 82.7, 96.7, 88.9, 80.4, 53.9]
noise_source_with_screen_2 = [66.2, 68.4, 67.4, 79.4, 84.8, 98.9, 98.8, 89.9, 61.3]
noise_source_with_screen_3 = [63.9, 67.4, 63.4, 78.6, 83.6, 96.9, 90.2, 81.8, 52.7]
noise_source_with_screen_4 = [58.8, 67.5, 62.9, 78.3, 83.4, 97, 90.7, 81.7, 54.8]
noise_source_screen_and_shell = [66.1, 67, 61.3, 64.4, 69.7, 79.6, 70.4, 53.8, 32.1]

# Преобразуем частоты в индексы для равного расстояния
x_indices = range(len(frequencies))

# ПС 80 по ISO
ps_80 = [93, 85, 77, 71, 66, 63, 61, 60, 58]

# Поправки для более высоких уровней (Δ)
delta_corrections = [0, -1, -2, -3, -5, -7]  # Поправки в дБ для каждой разности

# Функция для корректировки уровня звука на основе фона и разности уровней
def apply_background_and_level_correction_with_difference(noise_data, background_data, delta_corrections):
    corrected_data = []
    for i, (noise, background) in enumerate(zip(noise_data, background_data)):
        # Вычисляем разность между уровнем шума и фоновым уровнем
        level_difference = abs(noise - background)

        # Определяем поправку в зависимости от разности
        if level_difference >= 10:
            correction = delta_corrections[0]  # Для разности >= 10 дБ
        elif 6 <= level_difference <= 9:
            correction = delta_corrections[1]  # Для разности от 6 до 9 дБ
        elif 5 <= level_difference <= 4:
            correction = delta_corrections[2]  # Для разности от 5 до 4 дБ
        elif level_difference == 3:
            correction = delta_corrections[3]  # Для разности = 3 дБ
        elif level_difference == 2:
            correction = delta_corrections[4]  # Для разности = 2 дБ
        else:
            correction = delta_corrections[5]  # Для разности = 1 дБ
        corrected_data.append(max(noise, background) + correction)
    
    return corrected_data

# Применяем поправку на фоновый шум для всех наборов данных
corrected_noise_source_unprotected = apply_background_and_level_correction_with_difference(noise_source_unprotected, background_noise, delta_corrections)
corrected_noise_source_in_shell_1 = apply_background_and_level_correction_with_difference(noise_source_in_shell_1, background_noise, delta_corrections)
corrected_noise_source_in_shell_2 = apply_background_and_level_correction_with_difference(noise_source_in_shell_2, background_noise, delta_corrections)
corrected_noise_source_with_screen_1 = apply_background_and_level_correction_with_difference(noise_source_with_screen_1, background_noise, delta_corrections)
corrected_noise_source_with_screen_2 = apply_background_and_level_correction_with_difference(noise_source_with_screen_2, background_noise, delta_corrections)
corrected_noise_source_with_screen_3 = apply_background_and_level_correction_with_difference(noise_source_with_screen_3, background_noise, delta_corrections)
corrected_noise_source_with_screen_4 = apply_background_and_level_correction_with_difference(noise_source_with_screen_4, background_noise, delta_corrections)
corrected_noise_source_screen_and_shell = apply_background_and_level_correction_with_difference(noise_source_screen_and_shell, background_noise, delta_corrections)

# Функция для расчета эффективности
def calculate_efficiency(L1, L2):
    return [l1 - l2 for l1, l2 in zip(L1, L2)]

# Расчет эффективности для каждого источника шума
y_unprotected = calculate_efficiency(noise_source_unprotected, corrected_noise_source_unprotected)
efficiency_in_shell_1 = calculate_efficiency(corrected_noise_source_unprotected, corrected_noise_source_in_shell_1)
efficiency_in_shell_2 = calculate_efficiency(corrected_noise_source_unprotected, corrected_noise_source_in_shell_2)
efficiency_with_screen_1 = calculate_efficiency(corrected_noise_source_unprotected, corrected_noise_source_with_screen_1)
efficiency_with_screen_2 = calculate_efficiency(corrected_noise_source_unprotected, corrected_noise_source_with_screen_2)
efficiency_with_screen_3 = calculate_efficiency(corrected_noise_source_unprotected, corrected_noise_source_with_screen_3)
efficiency_with_screen_4 = calculate_efficiency(corrected_noise_source_unprotected, corrected_noise_source_with_screen_4)
efficiency_screen_and_shell = calculate_efficiency(corrected_noise_source_unprotected, corrected_noise_source_screen_and_shell)

# Настройка графика
plt.figure(figsize=(12, 6))

# Построение графиков для каждой из эффективностей
# plt.plot(x_indices, y_unprotected, label="Без средств защиты")
# plt.plot(x_indices, efficiency_in_shell_1, label="Кожух №1")
# plt.plot(x_indices, efficiency_in_shell_2, label="Кожух №2")
plt.plot(x_indices, efficiency_with_screen_1, label="Экран №1")
plt.plot(x_indices, efficiency_with_screen_2, label="Экран №2")
plt.plot(x_indices, efficiency_with_screen_3, label="Экран №3")
plt.plot(x_indices, efficiency_with_screen_4, label="Экран №4")
# plt.plot(x_indices, efficiency_screen_and_shell, label="Экран + Кожух")

# Настройки осей
x_indices = range(len(frequencies))
plt.xticks(x_indices, labels=[str(f) for f in frequencies])  # Подписи частот
plt.grid(True, which="both", linestyle="--", linewidth=0.5)  # Сетка на графике

# Подписи и легенда
plt.xlabel("Частота (Гц)", fontsize=12)  # Подпись оси X
plt.ylabel("Эффективность (дБ)", fontsize=12)  # Подпись оси Y
plt.legend()  # Легенда графика

# Сохранение графика с автоматическим именем
plt.tight_layout()
filename = f"efficiency_plot_{int(time.time())}.png"
plt.savefig(filename)

# Отображение графика
plt.show()
