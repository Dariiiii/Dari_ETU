from docx import Document

def extract_image_sizes(docx_path):
    """
    Extracts and prints the dimensions of images in a .docx file in cm.
    :param docx_path: Path to the .docx file.
    """
    # Загружаем документ
    doc = Document(docx_path)
    # Проходим по всем встроенным изображениям
    count =0
    print(len(doc.element))
    for shape in doc.inline_shapes:
        print(shape.type.value)
        # Проверяем, что это изображение
        if shape.type.value == 3:  # Проверяем, что это изображение
            count += 1
            width_emu = shape.width.cm  # Ширина в EMU
            height_emu = shape.height.cm  # Высота в EMU
            # Переводим размеры в сантиметры

            # Выводим информацию
            print("-"*50)
            print(f"Изображение {count}: Ширина = {width_emu:.2f} emu, Высота = {height_emu:.2f} emu")
            # print(f"Изображение {count}: Ширина = {width_cm:.2f} см, Высота = {height_cm:.2f} см")

# Пример использования:
docx_path = "2024ВКР030411КОЗИКОВ.docx"  # Замените на путь к вашему .docx файлу
extract_image_sizes(docx_path)
