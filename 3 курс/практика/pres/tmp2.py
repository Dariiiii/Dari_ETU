from PyPDF2 import PdfReader

# Откройте PDF-файл
reader = PdfReader('Презентация_ВКР_Алтухов.pdf')

# Прочитайте текст с первой страницы
text = reader.pages[13].extract_text().split('\n')

for t in text:
    print(t)
    print()
