from docx import Document
from docx.oxml.ns import qn
import time

# Константа для конвертации EMU в сантиметры
EMU_TO_CM = 360000

def extract_image_sizes(docx_path):
    """
    Extracts and prints the dimensions of images in a .docx file in cm.
    :param docx_path: Path to the .docx file.
    """
    # Загружаем документ
    doc = Document(docx_path)

    # Проход по всем параграфам документа
    size = []
    count = 0
    start_time = time.time()  # Начало измерения времени

    for paragraph in doc.paragraphs:
        # Проверяем, есть ли в параграфе встроенные объекты
        for run in paragraph.runs:
            if "graphic" in run._element.xml:  # может быть изображение
                # Извлечение бинарных данных изображения
                image_streams = run._element.findall('.//a:blip', namespaces={
                    'a': 'http://schemas.openxmlformats.org/drawingml/2006/main'})
                for image_stream in image_streams:
                    embed_id = image_stream.get(
                        '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed')
                    if embed_id:
                        count += 1
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

    end_time = time.time()  # Конец измерения времени
    elapsed_time = end_time - start_time

    print(f"Общее количество изображений: {count}")
    print(f"Время работы программы: {elapsed_time:.2f} секунд")
    print("Массив размеров изображений:")
    for img_size in size:
        print(img_size)

# Пример использования:
docx_path = "2024ВКР030411КОЗИКОВ.docx"  # Замените на путь к вашему .docx файлу
extract_image_sizes(docx_path)
