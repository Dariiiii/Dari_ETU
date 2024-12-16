from docx import Document
import time
import cv2
import pytesseract
import numpy as np
from PIL import Image
from io import BytesIO

# Константа для конвертации EMU в сантиметры
EMU_TO_CM = 360000

# Настройка Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_image_sizes(docx_path):
    doc = Document(docx_path)
    size = []
    count = 0
    start_time = time.time()

    for paragraph in doc.paragraphs:
        for run in paragraph.runs:
            if "graphic" in run._element.xml:
                image_streams = run._element.findall('.//a:blip', namespaces={
                    'a': 'http://schemas.openxmlformats.org/drawingml/2006/main'})
                for image_stream in image_streams:
                    embed_id = image_stream.get(
                        '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed')
                    if embed_id:
                        count += 1
                        image_part = doc.part.related_parts[embed_id]
                        image_data = image_part.blob
                        # process_image_data(image_data, count)
                        extent = run._element.find('.//wp:extent', namespaces={
                            'wp': 'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing'})
                        if extent is not None:
                            width_emu = int(extent.get('cx'))
                            height_emu = int(extent.get('cy'))
                            width_cm = width_emu / EMU_TO_CM
                            height_cm = height_emu / EMU_TO_CM
                            size.append({"height": height_cm, "width": width_cm})
                            process_image_data(image_data, count, width_cm, height_cm)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Общее количество изображений: {count}")
    print(f"Время: {elapsed_time:.2f} секунд")


def process_image_data(image_data, image_number, width_cm, height_cm):
    image = Image.open(BytesIO(image_data))
    res_ocr = analyze_with_pytesseract(image)
    text_p = sum(1 for char in res_ocr['text'] if not char.isspace())
    results = process_image(image)
    image_size = len(image_data)
    print('Image size:', image_size)
    # print(f"\nИтоговые результаты для изображения {image_number}:")
    # print(f'  Высота изображения: {height_cm:.4f}, ширина: {width_cm:.4f}')
    # print(f'  Текст (pytesseract): {res_ocr['text']}, Время: {res_ocr['ocr_time']:.4f} секунд')
    # print(f"  Дисперсия Laplacian: {results['laplacian_score']:.4f}, Время: {results['laplacian_time']:.4f} секунд")
    # print(f"  Энтропия: {results['entropy_score']:.4f}, Время: {results['entropy_time']:.4f} секунд")
    # print(f'{height_cm:.2f} {width_cm:.2f}')
    # print(f"{results['laplacian_score']:.2f}  {results['entropy_score']:.2f}")
    # print(f"{results['laplacian_score']:.2f}  {results['entropy_score']:.2f} {height_cm:.2f} {width_cm:.2f} {text_p}")

def analyze_with_pytesseract(image):
    start_time = time.time()
    try:
        img = np.array(image)
        if img is None:
            raise ValueError(f"Не удалось загрузить изображение")
        text = pytesseract.image_to_string(img, lang='rus+eng')
    except Exception as e:
        print(f'Ошибка при обработке изображения: {e}')
        text = ""

    end_time = time.time()
    elapsed_time = end_time - start_time
    return {
        'text': text,
        'ocr_time': elapsed_time
    }

def evaluate_laplacian(image):
    start_time = time.time()
    image_array = np.array(image)
    if image_array is None or image_array.size == 0:
        return None, None, None
    gray_image = cv2.cvtColor(image_array, cv2.COLOR_BGR2GRAY)
    laplacian_var = cv2.Laplacian(gray_image, cv2.CV_64F).var()
    end_time = time.time()
    processing_time = end_time - start_time
    return laplacian_var, processing_time

def evaluate_entropy(image):
    start_time = time.time()
    image_array = np.array(image)
    if image_array is None or image_array.size == 0:
        return None, None, None
    gray_image = cv2.cvtColor(image_array, cv2.COLOR_BGR2GRAY)
    hist, _ = np.histogram(gray_image.flatten(), bins=256, range=[0, 256])
    hist = hist / hist.sum()
    entropy = -np.sum(hist * np.log2(hist + 1e-10))  # +1e-10 чтобы избежать log(0)
    end_time = time.time()
    processing_time = end_time - start_time

    return entropy, processing_time

def process_image(image):
    image_array = np.array(image)
    if image_array.ndim == 2:
        image_array = cv2.cvtColor(image_array, cv2.COLOR_GRAY2BGR)
    image = Image.fromarray(image_array)
    laplacian_score, laplacian_time = evaluate_laplacian(image)
    entropy_score, entropy_time = evaluate_entropy(image)

    return {
        'laplacian_score': laplacian_score,
        'laplacian_time': laplacian_time,
        'entropy_score': entropy_score,
        'entropy_time': entropy_time
    }

def main():
    docx_path = "test_docx/test.docx" 
    extract_image_sizes(docx_path)

if __name__ == "__main__":
    main()
