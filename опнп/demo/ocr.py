import cv2
import pytesseract
import os
import time
import easyocr

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
image_folder = 'C:/Users/79064/Desktop/etu/4/opnp/test img d/'

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

def analyze_with_easyocr(image_folder, image_numbers):
    reader = easyocr.Reader(['ru', 'en'])
    extracted_texts = []
    start_time = time.time()

    for i in image_numbers:
        image_path = get_image_extension(i, image_folder)
        if image_path is None:
            print(f"Ошибка: Не удалось найти изображение с номером {i}")
            continue
        
        try:
            img = cv2.imread(image_path)
            if img is None:
                raise ValueError(f"Не удалось загрузить изображение {image_path}")

            result = reader.readtext(image_path)
            text = ' '.join([word[1] for word in result])
            extracted_texts.append(text)

        except Exception as e:
            print(f'Ошибка при обработке {image_path}: {e}')

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f'Время выполнения (EasyOCR): {elapsed_time:.2f} секунд')
    
    for i, text in enumerate(extracted_texts, start=image_numbers[0]):
        print(f'Изображение {i}:\n{text}\n')

def analyze_with_pytesseract(image_folder, image_numbers):
    extracted_texts = []
    start_time = time.time()

    for i in image_numbers:
        image_path = get_image_extension(i, image_folder)
        if image_path is None:
            print(f"Ошибка: Не удалось найти изображение с номером {i}")
            continue
        
        try:
            img = cv2.imread(image_path)
            if img is None:
                raise ValueError(f"Не удалось загрузить изображение {image_path}")
            text = pytesseract.image_to_string(img, lang='rus+eng')
            extracted_texts.append(text)

        except Exception as e:
            print(f'Ошибка при обработке {image_path}: {e}')

    end_time = time.time()
    elapsed_time = end_time - start_time
    
    print(f'Время выполнения (pytesseract): {elapsed_time:.2f} секунд')
    
    for i, text in enumerate(extracted_texts, start=image_numbers[0]):
        print(f'Изображение {i}:\n{text}\n')

# Указываем номера изображений для анализа
image_numbers = [1]  # Например, для изображений с номерами 1, 2 и 3
analyze_with_easyocr(image_folder, image_numbers)
analyze_with_pytesseract(image_folder, image_numbers)
