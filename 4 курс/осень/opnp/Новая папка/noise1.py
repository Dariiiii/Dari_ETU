import cv2
import numpy as np
import time

def calculate_blurriness(image):
    """Возвращает меру размытия изображения."""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()  # Дисперсия Лапласа
    return laplacian_var

def calculate_noise(image):
    """Возвращает меру шума изображения (стандартное отклонение)."""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    noise_stddev = np.std(gray)  # Стандартное отклонение
    return noise_stddev

def analyze_image(image_path):
    """Анализирует изображение на шум и размытие."""
    # Загрузка изображения
    image = cv2.imread(image_path)

    # Вычисляем шум и размытость
    noise_level = calculate_noise(image)
    blurriness_level = calculate_blurriness(image)

    # Вывод результатов
    print(f"Изображение: {image_path}")
    print(f"Уровень шума (стандартное отклонение): {noise_level:.2f}")
    if noise_level>50:
        print("плохо")
    print(f"Уровень размытия (дисперсия Лапласа): {blurriness_level:.2f}")
    if blurriness_level<50:
        print("двойка")
    print("-" * 50)

# Список изображений для анализа
image_paths = [
    '11.png',  # Путь к изображению 1
    '16.png',  # Путь к изображению 2
    '15.png',  # Путь к изображению 3
]

start_time = time.time()  # Считываем начальное время

# Проходим по списку изображений и анализируем каждое
for image_path in image_paths:
    analyze_image(image_path)

end_time = time.time()  # Считываем конечное время
execution_time = end_time - start_time  # Разница во времени выполнения
print(f"Время выполнения: {execution_time:.4f} секунд")
