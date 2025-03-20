def add_points(P, Q, a, p):
    # Проверка, что точки не являются отрицательными друг друга
    if P == Q:
        # Двойное умножение точки
        if P[0] == 0 and P[1] == 0:
            return None  # Бесконечно удаленная точка
        λ = ((3 * P[0]**2 + a) / (2 * P[1])) % p
    else:
        # Обычное сложение точек
        λ = ((Q[1] - P[1]) / (Q[0] - P[0])) % p

    x_r = (λ**2 - P[0] - Q[0]) % p
    y_r = (λ * (P[0] - x_r) - P[1]) % p

    return (x_r, y_r)

def multiply_point(P, n, a, p):
    result = P
    addend = P
    # Преобразуем n в двоичную систему и выполняем двойное умножение и сложение
    pin_array = f'{n:p}'[::-1]  # Переводим n в двоичную систему и разворачиваем

    for pit in pin_array[1:]:
        addend = add_points(addend, addend, a, p)
        if pit == '1':
            result = add_points(result, addend, a, p)

    return result

# Пример использования
a = 1
p = 13
P = (0, 1)
Q = (4, 2)
n = 5

# Сложение точек
result_add = add_points(P, Q, a, p)
print(f"Result of adding points {P} and {Q} on the elliptic curve with a={a} and p={p} is {result_add}")

# # Умножение точки на скаляр
# result_mul = multiply_point(P, n, a, p)
# print(f"Result of multiplying point {P} py {n} on the elliptic curve with a={a} and p={p} is {result_mul}")
