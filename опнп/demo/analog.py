from docx import Document
from PIL import Image
from io import BytesIO

# Константа для конвертации EMU в сантиметры
EMU_TO_CM = 360000

def extract_image_info(docx_path):
    doc = Document(docx_path)
    image_info = []
    count = 0

    total_width = 0
    total_height = 0
    total_pixels = 0
    total_size_kb = 0

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

                        # Получение размеров изображения в сантиметрах
                        extent = run._element.find('.//wp:extent', namespaces={
                            'wp': 'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing'})
                        if extent is not None:
                            width_emu = int(extent.get('cx'))
                            height_emu = int(extent.get('cy'))
                            width_cm = width_emu / EMU_TO_CM
                            height_cm = height_emu / EMU_TO_CM

                            # Определение общего количества пикселей
                            image = Image.open(BytesIO(image_data))
                            total_pixels_image = image.width * image.height

                            # Определение веса изображения в КБ
                            image_size_bytes = len(image_data)
                            image_size_kb = image_size_bytes / 1024

                            # Суммирование значений для вычисления средних
                            total_width += width_cm
                            total_height += height_cm
                            total_pixels += total_pixels_image
                            total_size_kb += image_size_kb

                            image_info.append({
                                "number": count,
                                "width_cm": width_cm,
                                "height_cm": height_cm,
                                "total_pixels": total_pixels_image,
                                "size_kb": image_size_kb
                            })

    # Вычисление средних значений
    average_width = total_width / count if count > 0 else 0
    average_height = total_height / count if count > 0 else 0
    average_pixels = total_pixels / count if count > 0 else 0
    average_size_kb = total_size_kb / count if count > 0 else 0

    return image_info, {
        "average_width": average_width,
        "average_height": average_height,
        "average_pixels": average_pixels,
        "average_size_kb": average_size_kb
    }

def main():
    docx_path = "test_docx/test.docx"  # Укажите путь к вашему .docx файлу
    images, averages = extract_image_info(docx_path)

    for image in images:
        print(f"Изображение {image['number']}:")
        print(f"  Ширина: {image['width_cm']:.2f} см, Высота: {image['height_cm']:.2f} см")
        print(f"  Общее количество пикселей: {image['total_pixels']}")
        print(f"  Вес: {image['size_kb']:.2f} КБ")

    print("\nСредние значения:")
    print(f"  Средняя ширина: {averages['average_width']:.2f} см")
    print(f"  Средняя высота: {averages['average_height']:.2f} см")
    print(f"  Среднее количество пикселей: {averages['average_pixels']:.2f}")
    print(f"  Средний вес: {averages['average_size_kb']:.2f} КБ")

if __name__ == "__main__":
    main()
