def hex_to_dec_pairs(hex_string):
    # Убедимся, что длина строки четная
    if len(hex_string) % 2 != 0:
        raise ValueError("Длина строки должна быть четной")

    # Разделим строку на пары по два символа
    pairs = [hex_string[i:i+2] for i in range(0, len(hex_string), 2)]

    # Переведем каждую пару из шестнадцатеричной системы в десятичную
    dec_values = [int(pair, 16) for pair in pairs]

    return dec_values

# Пример использования
hex_string = "17b448831138bba393f2fe7e22e41b95"
dec_values = hex_to_dec_pairs(hex_string)
print(dec_values)
# dec_values = (" ").join(dec_values)
print(dec_values)  # Вывод: [26, 43, 60, 77]
a = '106 32 97 1 167 67 152 34 180 19 177 122 71 31 129 215'
a = [int(num) for num in a.split(' ')]
def dec_to_hex_pairs(dec_values):
    # Переведем каждое десятичное число в шестнадцатеричную строку
    hex_pairs = [format(value, '02x') for value in dec_values]

    # Объединим все шестнадцатеричные строки в одну строку
    hex_string = ''.join(hex_pairs)

    return hex_string

# Пример использования
# hex_string = dec_to_hex_pairs(dec_values)
hex_string = dec_to_hex_pairs(a)
print(hex_string)  # Вывод: "1a2b3c4d"

