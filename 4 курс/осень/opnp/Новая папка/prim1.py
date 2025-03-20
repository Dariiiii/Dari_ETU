import cv2
import numpy as np
import matplotlib.pyplot as plt
import time

# Функция для распознавания геометрических примитивов
def detect_shapes(image_path):
    # Считываем изображение
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Переводим в оттенки серого
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)     # Размываем изображение для снижения шума

    # Применяем бинаризацию методом Оцу
    _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Находим контуры на изображении
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Проходим по каждому найденному контуру
    for contour in contours:
        # Приблизим контур (чтобы сгладить углы)
        approx = cv2.approxPolyDP(contour, 0.04 * cv2.arcLength(contour, True), True)

        # Определяем количество вершин
        vertices = len(approx)
        
        # Определение примитивов на основе количества вершин
        shape = ""
        if vertices == 3:
            shape = "3"
        elif vertices == 4:
            # Проверяем, является ли форма прямоугольником
            (x, y, w, h) = cv2.boundingRect(approx)
            aspect_ratio = w / float(h)
            shape = "4" if 0.95 <= aspect_ratio <= 1.05 else "4+"
        elif vertices > 4:
            # Проверяем, является ли форма кругом
            (x, y), radius = cv2.minEnclosingCircle(contour)
            circle_area = np.pi * (radius ** 2)
            contour_area = cv2.contourArea(contour)
            if 0.8 <= contour_area / circle_area <= 1.2:
                shape = "0"
        
        # Рисуем найденный примитив на изображении
        if shape:
            cv2.drawContours(image, [approx], -1, (0, 255, 0), 2)  # Контур зеленым цветом
            # Пишем имя фигуры на изображении
            cv2.putText(image, shape, (approx[0][0][0], approx[0][0][1] - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

    return image

# Список изображений для анализа
image_paths = [
    '11.png',  # Путь к изображению 1
    '15.png',  # Путь к изображению 2
    '16.png',  # Путь к изображению 3
]

start_time = time.time()  # Считываем начальное время

# Проходим по списку изображений и ищем примитивы
for image_path in image_paths:
    print(f"Анализ геометрических примитивов на изображении: {image_path}")
    
    # Получаем изображение с найденными фигурами
    result_image = detect_shapes(image_path)

    # Визуализация изображения
    plt.figure(figsize=(10, 6))
    plt.imshow(cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB))  # Конвертируем в RGB для корректного отображения
    plt.title(f"Геометрические примитивы на изображении {image_path}")
    plt.axis('off')
    plt.show()
    print("-" * 50)

end_time = time.time()  # Считываем конечное время
execution_time = end_time - start_time  # Разница во времени выполнения
print(f"Время выполнения: {execution_time:.4f} секунд")
