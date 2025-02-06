from docx import Document
import cv2
import pytesseract
import numpy as np

EMU_TO_CM = 360000
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_image_sizes(docx_path):
    doc = Document(docx_path)
    size = []
    for paragraph in doc.paragraphs:
        for run in paragraph.runs:
            if "graphic" in run._element.xml:
                image_streams = run._element.findall('.//a:blip', namespaces={
                    'a': 'http://schemas.openxmlformats.org/drawingml/2006/main'})
                for image_stream in image_streams:
                    embed_id = image_stream.get(
                        '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed')
                    if embed_id:
                        image_part = doc.part.related_parts[embed_id]
                        image_data = image_part.blob
                        extent = run._element.find('.//wp:extent', namespaces={
                            'wp': 'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing'})
                        if extent is not None:
                            width_emu = int(extent.get('cx'))
                            height_emu = int(extent.get('cy'))
                            width_cm = width_emu / EMU_TO_CM
                            height_cm = height_emu / EMU_TO_CM
                            size.append({"height": height_cm, "width": width_cm})
                            process_image_data(image_data, width_cm, height_cm)

def process_image_data(image_data, width_cm, height_cm):
    image_array = np.frombuffer(image_data, dtype=np.uint8)
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
    res_ocr = analyze_with_pytesseract(image)
    # text_p = sum(1 for char in res_ocr['text'] if not char.isspace())
    results = process_image(image)
    print(f'  Высота изображения: {height_cm:.4f}, ширина: {width_cm:.4f}')
    print(f"  Дисперсия Laplacian: {results['laplacian_score']:.4f}")
    print(f"  Энтропия: {results['entropy_score']:.4f}")

def analyze_with_pytesseract(image):
    try:
        if image is None:
            raise ValueError("Не удалось загрузить изображение")
        text = pytesseract.image_to_string(image, lang='rus+eng')
    except Exception as e:
        print(f'Ошибка при обработке изображения: {e}')
        text = ""

    return {
        'text': text
    }


def process_image(image):
    if image is None or image.size == 0:
        return None, None
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    laplacian_score = cv2.Laplacian(gray_image, cv2.CV_64F).var()
    
    hist, _ = np.histogram(gray_image.flatten(), bins=256, range=[0, 256])
    hist = hist / hist.sum()
    entropy_score = -np.sum(hist * np.log2(hist + 1e-10))
    
    return {
        'laplacian_score': laplacian_score,
        'entropy_score': entropy_score
    }


def main():
    docx_path = "test_docx/test.docx" 
    extract_image_sizes(docx_path)

if __name__ == "__main__":
    main()
