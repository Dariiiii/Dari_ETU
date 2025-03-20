def matrix_mod_26(matrix):
    """
    Возвращает новую матрицу, где каждый элемент оригинальной матрицы
    взят по модулю 26.

    :param matrix: Двумерный список (матрица)
    :return: Новая матрица с элементами по модулю 26
    """
    return [[element % 26 for element in row] for row in matrix]

# Пример использования
original_matrix = [
    [228, 96],
    [208, 106],
    [7, 4],
    [151, 52]
]

result_matrix = matrix_mod_26(original_matrix)

# Вывод результата
for row in result_matrix:
    print(*row)