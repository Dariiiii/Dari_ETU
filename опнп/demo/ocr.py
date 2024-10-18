import cv2
import pytesseract
import os
import time

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
image_folder = 'C:/Users/79064/Desktop/etu/4/opnp/test img/'
extracted_texts = []

start_time = time.time()

for i in range(4, 10):
    image_path = os.path.join(image_folder, f'{i}.png')
    
    try:
        img = cv2.imread(image_path)
        if img is None:
            raise ValueError(f"Не удалось загрузить изображение {image_path}")

        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(gray_img)
        extracted_texts.append(text)
        print(f'Изображение {i}:')
        print(text)
    except Exception as e:
        print(f'Ошибка при обработке {image_path}: {e}')

end_time = time.time() 
elapsed_time = end_time - start_time  

for i, text in enumerate(extracted_texts, start=4):
    print(f'Изображение {i}:\n{text}\n\n')

print(f'Время выполнения: {elapsed_time:.2f} секунд')