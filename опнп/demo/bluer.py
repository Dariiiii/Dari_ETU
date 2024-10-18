import cv2
import os
import time

image_folder = 'C:/Users/79064/Desktop/etu/4/opnp/test img/'

def calculate_blur_level(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return cv2.Laplacian(gray_image, cv2.CV_64F).var()  # Дисперсия градиента изображения

start_time = time.time()

for i in range(1, 11):
    image_path = os.path.join(image_folder, f'{i}.png')
    
    try:
        img = cv2.imread(image_path)
        
        if img is None:
            raise ValueError(f"Не удалось загрузить изображение: {image_path}")
        blur_level = calculate_blur_level(img)
        threshold_blur = 100  
        end_time = time.time()  
        if blur_level < threshold_blur:
            print(f'Изображение {i} размыто (уровень блюра: {blur_level:.2f})')
        else:
            print(f'Изображение {i} не размыто (уровень блюра: {blur_level:.2f})')

    except Exception as e:
        print(f'Ошибка при обработке {image_path}: {e}')

elapsed_time = end_time - start_time        
print(f'Время выполнения: {elapsed_time:.2f} секунд')