from predobl import *
# дихотомия
# eps = 0.3
# a0 = 1.0
# b0 = 10.0
# def fff(x):
#     return (x - 2.5) ** 2
#
# def initial():
#     # начальная установка
#     a = a0
#     b = b0
#     val = 'проведена'
#     return a, b
#
# def a1(a, b):
#     # дихотомия
#     val = 'проведена'
#     x = (a + b) / 2
#     x1 = x - eps / 2
#     x2 = x + eps / 2
#     return x1, x2
#
#
# def a2(a, x1, x2, b):
#     # информация
#     val = 'выведена'
#     print('a=', a, 'f=', fff(a))
#     print('x1=', x1, 'f=', fff(x1))
#     print('x2=', x2, 'f=', fff(x2))
#     print('b=', b, 'f=', fff(b))
#     return val
#
#
# def a3(a, x1, x2):
#     # граница а
#     if fff(x1) > fff(x2):
#         a = x1
#     # if abs(a - float(par1)) <= eps:
#     #    val = 'да'
#     # else:
#     #    val = 'нет'
#     return a
#
#
# def a4(b, x1, x2):
#     # граница b
#     if fff(x1) < fff(x2):
#         b = x2
#     # if abs(b - float(par1)) <= eps:
#     #    val = 'да'
#     # else:
#     #    val = 'нет'
#     return b
#
#
# def a5(a, b):
#     # проверка окончания
#     if abs(a - b) <= 2 * eps + eps / 100:
#         val = 'да'
#     else:
#         val = 'нет'
#     return val
#
# def a6(x1, x2):
#     # Результаты
#     val = 'да'
#     print('Результаты')
#     print('x1=', x1, ' f(x1)=', fff(x1))
#     print('x2=', x2, ' f(x2)=', fff(x2))
#     return val


print('')
auto = False
flag = True
if auto == False:
    print('Будет проведена начальная установка ')
a, b = initial()     # начальная установка
if auto == False:
    print('Будет проведена ДИХОТОМИЯ')
    print('Подсказка дихотомия: x = (a + b) / 2  x1 = x - eps / 2  x2 = x + eps / 2')
x1, x2 = a1(a, b)  # дихотомия
if auto == False:
    print('Показ обновленной информации')
a2(a, x1, x2, b)   # информация
while flag:
    if auto == False:
        print('Определение границы_a')
        print('Подсказка граница_а :::  if  f(x1)>f(x2) then a:=x1')
    a =a3(a, x1, x2)  # граница_a
    if auto == False:
        print('Показ обновленной информации')
    a2(a, x1, x2, b)   # информация
    if auto == False:
        print('Определение границы_b')
        print('Подсказка граница_б :::  if  f(x1)<f(x2) then b:=x2')
    b = a4(b, x1, x2)   # граница_b
    if auto == False:
        print('Показ обновленной информации')
    a2(a, x1, x2, b)   # информация
    if auto == False:
        print('Будет проведена ДИХОТОМИЯ')
        print('Подсказка дихотомия: x = (a + b) / 2  x1 = x - eps / 2  x2 = x + eps / 2')
    x1, x2 = a1(a, b)  # дихотомия
    if auto == False:
        print('Показ обновленной информации')
    a2(a, x1, x2, b)   # информация
    if auto == False:
        print('Проверка окончания')
        print('Точность достигнута? (да/нет)')
        print('Подсказка конец :::  if abs(a-b)<= 2*eps+eps/100 then да else нет')
    val = a5(a, b)
    if auto == False:
        print('val= ', val)
    if val == 'да':
        flag = False
if auto == False:
    print('результаты')
a6(x1, x2)