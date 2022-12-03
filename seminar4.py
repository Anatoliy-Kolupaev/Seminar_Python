import math
# 1 - Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.

str = [int(i) for i in input('Введите числа через пробел: ').split()]
print(f'Большее = {max(str)}, Mеньшее = {min(str)}')

# 2 - Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1) с помощью математических формул нахождения корней квадратного уравнения

# 2) с помощью дополнительных библиотек Python

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))


def quadratic_equation(a, d, c):
    """Нахождение корней квадратного уравнения"""

    discr = math.pow(b, 2) - 4 * a * c
    print("Дискриминант D =", discr)
    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        print(f'x1 = {x1}, x2 = {x2}')
    elif discr == 0:
        x = -b / (2 * a)
        print("x = ", x)
    else:
        print("Корней нет")


quadratic_equation(a, b, c)

# 3 - Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

a, b = int(input()), int(input())
c = max(a, b)
while c > 0:
    if c % a == 0 and c % b == 0:
        print(f'Наименьшее общее кратное {c}')
        break
    else:
        c += 1

# вариант 2

a = int(input('Введите первое число: '))
b = int(input('Введите первое число: '))
max_val = a if a > b else b
count = 1
while True:
    if (max_val // a == max_val / a) and (max_val // b == max_val / b):
        print(max_val)
        break
    else:
        count += 1
        max_val = a if a > b else b
        max_val *= count
