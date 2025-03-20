# Читаем текст из файла
with open('text.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Создаем 4 файла для записи
files = [open(f'part_{i + 1}.txt', 'w', encoding='utf-8') for i in range(4)]

# Записываем символы в файлы по модулю 4
for index, char in enumerate(text):
    files[index % 4].write(char)

# Закрываем все файлы
for f in files:
    f.close()
