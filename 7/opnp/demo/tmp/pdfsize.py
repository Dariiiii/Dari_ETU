import fitz  # PyMuPDF

def count_images_in_pdf(pdf_path):
    # Открываем PDF-документ
    pdf_document = fitz.open(pdf_path)

    total_images = 0

    # Перебираем все страницы в документе
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        images = page.get_images(full=True)
        total_images += len(images)

    return total_images

# Путь к вашему PDF-документу
pdf_path = '2024ВКР030411КОЗИКОВ.pdf'

# Подсчитываем количество изображений в документе
image_count = count_images_in_pdf(pdf_path)
print(f"Количество изображений в документе: {image_count}")
