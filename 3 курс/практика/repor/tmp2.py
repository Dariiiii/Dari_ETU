import re
# Текст для разделения
text = "Пример текста, с разными.разделителями; и: символами!"

# Разделители: пробел, запятая, точка, точка с запятой, двоеточие
delimiters = ' ', ',', '.', ';', ':'

# Создаем шаблон для разделителей
regexPattern = '|'.join(map(re.escape, delimiters))

# Разделяем текст
words = re.split(regexPattern, text)

print(words)