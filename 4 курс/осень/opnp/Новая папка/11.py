import tensorflow as tf
import numpy as np
import cv2
from PIL import Image
from IPython.display import display

# Загрузка модели
model_dir = "C:/Users/79064/Desktop/ssd_mobilenet_v2_fpnlite_640x640_coco17_tpu-8/saved_model"
model = tf.saved_model.load(model_dir)

# Функция для обработки изображения
def load_image_into_numpy_array(path):
    return np.array(Image.open(path))

# Обработка изображения
def run_inference_for_single_image(model, image):
    image = np.asarray(image)
    input_tensor = tf.convert_to_tensor(image)
    input_tensor = input_tensor[tf.newaxis, ...]  # Добавление размерности
    detections = model(input_tensor)
    return detections

# Основная часть программы
image_path = '12.png'  # Путь к изображению
image_np = load_image_into_numpy_array(image_path)
detections = run_inference_for_single_image(model, image_np)

# Вывод результатов
# print(detections)

# Визуализация результатов
# Извлечение значения num_detections как скалярного
num_detections = int(detections['num_detections'][0].numpy())  # Используем [0] для извлечения

for i in range(num_detections):
    score = detections['detection_scores'][0][i].numpy()
    if score > 0.5:  # Фильтрация по порогу
        box = detections['detection_boxes'][0][i].numpy()
        print(f'Обнаружен объект с вероятностью {score} в координатах {box}')
print("\n================================")
