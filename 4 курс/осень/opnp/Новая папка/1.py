from sympy import symbols, integrate, Abs, sign

# Определяем переменные
x = symbols('x')

# Начальные условия
U_initial = -1.1 * Abs(x)**5  # U(x, 0)
U_t_initial = 9.6 * Abs(x)**3  # U_t(x, 0)

def calculate_f_and_g():
    # Найдем f'(x)
    f_prime = -0.5 * (1.6 * Abs(x)**3 + 5.5 * Abs(x)**4 * sign(x))
    
    # Интегрируем для нахождения f(x)
    f_x = integrate(f_prime, x)  # f(x)
    
    # Определяем g(x) через f(x)
    g_x = U_initial - f_x  # g(x)
    
    return f_x, g_x

def evaluate_integrals(expr, lower_limit, upper_limit):
    """ Функция для вычисления интеграла и возвращения его значения """
    return integrate(expr, (x, lower_limit, upper_limit))

def wave_equation_solution(x_value, t_value, c):
    # Получаем функции f(x) и g(x)
    f_x, g_x = calculate_f_and_g()

    # Подставляем значения
    f_value_expr = f_x.subs(x, x_value - c * t_value)  # f(x - ct)
    g_value_expr = g_x.subs(x, x_value + c * t_value)  # g(x + ct)

    # Вычисляем значения интегралов
    f_integral_value = evaluate_integrals(f_value_expr, -4, x_value - c * t_value)
    g_integral_value = evaluate_integrals(g_value_expr, -4, x_value + c * t_value)

    # Суммируем значения
    result = f_integral_value + g_integral_value

    # Возвращаем результат
    return float(result)

# Пример использования
x_value = 2
t_value = 1
c = 6  # Скорость волны

# Решение задачи
U_2_1 = wave_equation_solution(x_value, t_value, c)
print(f"Результат U(2, 1): {U_2_1}")
