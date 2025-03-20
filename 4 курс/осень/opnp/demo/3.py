import cv2
import numpy as np
import os
import time
from skimage import io
from brisque import BRISQUE

def get_image_extension(image_number, image_folder):
    """
    Определяет формат изображения (JPEG или PNG) по его расширению.
    """
    possible_extensions = ['jpg', 'jpeg', 'png']
    for ext in possible_extensions:
        image_path = os.path.join(image_folder, f"{image_number}.{ext}")
        if os.path.exists(image_path):
            return image_path
    return None

def evaluate_brisque(image_path):
    start_time = time.time()
    image = io.imread(image_path)
    brisque_model = BRISQUE()
    score = brisque_model.score(image)
    end_time = time.time()
    
    processing_time = end_time - start_time
    quality = "Хорошее" if score < 50 else "Плохое"
    
    return score, processing_time, quality

def evaluate_laplacian(image_path):
    start_time = time.time()
    image = cv2.imread(image_path)
    
    if image is None or image.size == 0:
        return None, None, None
    
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    laplacian_var = cv2.Laplacian(gray_image, cv2.CV_64F).var()
    end_time = time.time()
    
    processing_time = end_time - start_time
    quality = "Хорошее" if laplacian_var > 100 else "Плохое"
    
    return laplacian_var, processing_time, quality

def evaluate_entropy(image_path):
    start_time = time.time()
    image = cv2.imread(image_path)
    
    if image is None or image.size == 0:
        return None, None, None
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    hist, _ = np.histogram(gray_image.flatten(), bins=256, range=[0, 256])
    hist = hist / hist.sum() 

    entropy = -np.sum(hist * np.log2(hist + 1e-10))  # +1e-10 чтобы избежать log(0)

    end_time = time.time()
    processing_time = end_time - start_time

    quality = "Хорошее" if entropy > 4.5 else "Плохое" 
    
    return entropy, processing_time, quality

def process_image(image_path):
    brisque_score, brisque_time, brisque_quality = evaluate_brisque(image_path)
    laplacian_score, laplacian_time, laplacian_quality = evaluate_laplacian(image_path)
    entropy_score, entropy_time, entropy_quality = evaluate_entropy(image_path)
    
    return {
        'brisque_score': brisque_score,
        'brisque_time': brisque_time,
        'brisque_quality': brisque_quality,
        'laplacian_score': laplacian_score,
        'laplacian_time': laplacian_time,
        'laplacian_quality': laplacian_quality,
        'entropy_score': entropy_score,
        'entropy_time': entropy_time,
        'entropy_quality': entropy_quality
    }

image_folder = 'C:/Users/79064/Desktop/etu/4/opnp/test img d/'
results_all_images = []

for i in range(1, 14): 
    image_path = get_image_extension(i, image_folder)
    
    if image_path is None:
        print(f"Ошибка: Не удалось найти изображение с номером {i}")
        continue
    
    results = process_image(image_path)
    results_all_images.append((f'Картинка {i}', results)) 

print("\nИтоговые результаты:")
for image_name, results in results_all_images:
    print(f"\n{image_name}:")
    print(f"  Дисперсия Laplacian: {results['laplacian_score']:.4f}, Качество: {results['laplacian_quality']}, Время: {results['laplacian_time']:.4f} секунд")
    print(f"  Оценка BRISQUE: {results['brisque_score']:.4f}, Качество: {results['brisque_quality']}, Время: {results['brisque_time']:.4f} секунд")
    print(f"  Энтропия: {results['entropy_score']:.4f}, Качество: {results['entropy_quality']}, Время: {results['entropy_time']:.4f} секунд")
    print(f"{results['laplacian_score']:.2f} {results['brisque_score']:.2f} {results['entropy_score']:.2f}")