from docx import Document
from PIL import Image
import io

def extract_images(docx_path, output_dir):
    """
    Extracts images from a .docx file and saves them in the original format.
    :param docx_path: Path to the .docx file.
    :param output_dir: Directory to save the extracted images.
    """
    # Загружаем документ
    doc = Document(docx_path)

    # Проход по всем параграфам документа
    count = 0
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

                        # Сохраняем изображение в исходном формате
                        image = Image.open(io.BytesIO(image_data))
                        image_path = f"{output_dir}/image_{count}.{image.format.lower()}"
                        # image.save(image_path)
                        print(f"Изображение {count} размер {image.height.real} * {image.width}")

# Пример использования:
docx_path = "2024ВКР030411КОЗИКОВ.docx"  # Замените на путь к вашему .docx файлу
output_dir = "extracted_images"  # Директория для сохранения изображений
extract_images(docx_path, output_dir)
