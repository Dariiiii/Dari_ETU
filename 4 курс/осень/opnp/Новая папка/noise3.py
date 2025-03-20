import cv2
import numpy as np
import time
from skimage import img_as_float
from skimage import io
import brisque  # Убедитесь, что библиотека установлена
import niqe  # Убедитесь, что библиотека установлена

# Функция для оценки качества с использованием BRISQUE
def assess_quality_brisque(image_path):
    try:
        # Загружаем изображение и проверяем его формат
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError("Изображение не загружено. Проверьте путь.")
        
        # Преобразуем изображение в нужный формат
        if len(image.shape) == 3 and image.shape[2] == 4:  # Если изображение с альфа-каналом
            image = cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)
        score = brisque.BRISQUE().score(image_path)
    except Exception as e:
        print(f"Ошибка при оценке BRISQUE: {e}")
        score = None
    return score

# Функция для оценки качества с использованием NIQE
def assess_quality_niqe(image_path):
    try:
        # Загружаем изображение
        image = io.imread(image_path)
        if len(image.shape) == 3 and image.shape[2] == 4:  # Если изображение с альфа-каналом
            image = cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)
        
        score = niqe.niqe(img_as_float(image))
    except Exception as e:
        print(f"Ошибка при оценке NIQE: {e}")
        score = None
    return score

# Основная часть программы
image_paths = ['11.png', '15.png', '16.png']  # Путь к изображениям
start_time = time.time()  # Считываем начальное время

for image_path in image_paths:
    print(f"Анализ изображения: {image_path}")

    # Оценка качества изображения с использованием BRISQUE
    brisque_score = assess_quality_brisque(image_path)
    if brisque_score is not None:
        print(f"BRISQUE Score: {brisque_score}")
    else:
        print("Ошибка при оценке BRISQUE.")

    # Оценка качества изображения с использованием NIQE
    niqe_score = assess_quality_niqe(image_path)
    if niqe_score is not None:
        print(f"NIQE Score: {niqe_score}")
    else:
        print("Ошибка при оценке NIQE.")

    print("-" * 50)

end_time = time.time()  # Считываем конечное время
execution_time = end_time - start_time  # Разница во времени выполнения
print(f"Время выполнения: {execution_time:.4f} секунд")
