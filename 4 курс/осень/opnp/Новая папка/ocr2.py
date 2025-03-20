import pytesseract
from PIL import Image
import time

# Укажите путь к установленному tesseract (например, для Windows)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

start_time = time.time()  # Считываем начальное время

# Список изображений для анализа (замените на свои пути к изображениям)
image_paths = [
    '11.png',  # Путь к изображению 1
    '12.png',  # Путь к изображению 2
    '13.png',  # Путь к изображению 3
]

# Проходим по списку изображений и распознаем текст
for image_path in image_paths:
    print(f"Распознавание текста на изображении: {image_path}")
    # Открытие изображения
    img = Image.open(image_path)

    # Распознавание текста с помощью pytesseract
    result = pytesseract.image_to_string(img, lang='eng+rus')  # 'eng+rus' для английского и русского языков

    # Вывод результата
    print("Текст, обнаруженный на изображении:")
    print(result)
    print("-" * 50)

end_time = time.time()  # Считываем конечное время

execution_time = end_time - start_time  # Разница во времени выполнения
print(f"Время выполнения: {execution_time:.4f} секунд")
