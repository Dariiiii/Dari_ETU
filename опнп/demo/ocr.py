import cv2
import pytesseract
import os
import time
import easyocr

# Укажите путь к Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
image_folder = 'C:/Users/79064/Desktop/etu/4/opnp/test img/'

def analyze_with_easyocr(image_folder, image_numbers):
    reader = easyocr.Reader(['ru', 'en'])
    extracted_texts = []
    start_time = time.time()

    for i in image_numbers:
        image_path = os.path.join(image_folder, f'{i}.png')
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
        image_path = os.path.join(image_folder, f'{i}.png')
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

    

image_numbers = [14]

analyze_with_easyocr(image_folder, image_numbers)
analyze_with_pytesseract(image_folder, image_numbers)