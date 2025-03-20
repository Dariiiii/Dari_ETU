import torch
import numpy as np
from PIL import Image
import time
from torchvision import models, transforms

# Проверяем доступность CUDA
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Загрузка предобученной модели для классификации изображений
model = models.resnet50(pretrained=True).to(device)
model.eval()  # Устанавливаем модель в режим оценки

# Трансформации для изображения
transform = transforms.Compose([
    transforms.Resize((224, 224)),  # Приведение изображения к размеру 224x224
    transforms.ToTensor(),  # Преобразование в тензор
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),  # Нормализация
])

# Функция для загрузки изображения и преобразования его в тензор
def load_image(image_path):
    img = Image.open(image_path).convert('RGB')  # Конвертация в цветное изображение
    return transform(img).unsqueeze(0).to(device)  # Добавляем размерность для батча

# Функция для оценки уровня шума и размытия
def assess_image(image_tensor):
    with torch.no_grad():
        output = model(image_tensor)
        probs = torch.nn.functional.softmax(output[0], dim=0)
    
    # Определяем класс с максимальной вероятностью
    class_index = torch.argmax(probs).item()
    confidence = probs[class_index].item()

    # Оценка уровня шума и размытия
    if class_index == 0:  # Пример для класса 'загрузки' (например, 'птица')
        quality_score = "Высокое качество изображения"
    elif class_index in [1, 2]:  # Примеры для 'шумных' классов
        quality_score = "Низкое качество изображения: возможный шум"
    else:
        quality_score = "Неопределенное качество изображения"

    return class_index, confidence, quality_score

# Основная часть программы
image_paths = ['11.png', '15.png', '16.png']  # Путь к изображениям
start_time = time.time()  # Считываем начальное время

for image_path in image_paths:
    print(f"Анализ изображения: {image_path}")
    
    image_tensor = load_image(image_path)
    class_index, confidence, quality_score = assess_image(image_tensor)

    # Вывод результатов
    print(f"Класс: {class_index}, Вероятность: {confidence:.4f}, Оценка: {quality_score}")
    print("-" * 50)

end_time = time.time()  # Считываем конечное время
execution_time = end_time - start_time  # Разница во времени выполнения
print(f"Время выполнения: {execution_time:.4f} секунд")
