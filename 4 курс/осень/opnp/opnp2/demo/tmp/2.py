import cv2
import numpy as np
import time
import os
from skimage import color
from skimage.measure import shannon_entropy
from brisque import BRISQUE  # Убедитесь, что библиотека BRISQUE установлена


# Метод для определения размытия на основе дисперсии Лапласиана
def blur_detection_laplacian(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()
    is_blurry = laplacian_var < 100
    return "Размытие (Метод Лапласиана)", {
        "Размытие": "Да" if is_blurry else "Нет",
        "Дисперсия": round(laplacian_var, 2)
    }

# Оценка качества через BRISQUE
def brisque(image):
    bq = BRISQUE()
    score = bq.score(image)
    quality = "читаемо" if score < 70 else "Гавно"  # Базовая оценка для BRISQUE
    return "BRISQUE", {"Оценка": round(score, 2), "Качество": quality}


# Обработка изображения с применением выбранных методов
        # blur_detection_laplacian,
def process_image(image):
    methods = [

        brisque
    ]

    results = []
    for method in methods:
        start_time = time.time()
        name, result = method(image)
        end_time = time.time()
        execution_time = end_time - start_time
        results.append((name, result, execution_time))
    
    return results

# Основная функция для обработки изображений из папки
def main():
    image_folder = 'C:/Users/79064/Desktop/etu/4/opnp/test img d/'  # Папка с изображениями
    results_all_images = []  # Список для хранения результатов всех изображений
    
    # Процесс обработки изображений с именами от 1.png до 10.png
    for i in range(10, 12):  # Для изображений с именами 1.png, 2.png, ..., 10.png
        image_path = os.path.join(image_folder, f'{i}.jpg')
        image = cv2.imread(image_path)
        
        if image is None:
            print(f"Ошибка: не удалось загрузить изображение {image_path}")
            continue
        
        # Обработка изображения
        results = process_image(image)
        results_all_images.append((image_path, results))  # Сохраняем результаты для текущего изображения
    
    # Вывод результатов
    for image_path, results in results_all_images:
        print(f"\nРезультаты анализа качества изображения: {os.path.basename(image_path)}")  # Выводим имя файла
        print("="*50)
        for name, result, exec_time in results:
            print(f"{name}:")
            for key, value in result.items():
                print(f"  {key}: {value}")
            print(f"  Время выполнения: {exec_time:.4f} секунд")
            print("-"*50)

# Точка входа
if __name__ == "__main__":
    main()
