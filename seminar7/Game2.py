from random import *


def game_conditions():
    """Условия игры"""
    print()
    print('Условие игры: На столе лежит 117 конфета. Играют два игрока делая ход друг после друга.')
    print('Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.')
    print('Все конфеты оппонента достаются сделавшему последний ход.')
    print()


def user_choice():
    """Выбор режима игры"""
    choice_user = int(input(
        'Если вы хотите играть против компьютера нажмите 1 \nЕсли хотите играть против друга нажмите 2: '))
    if choice_user == 2:
        user1 = input("Введите имя 1го игрока: ")
        user2 = input("Введите имя 2го игрока: ")
    else:
        user1 = input("Введите ваше имя: ")
        user2 = 'БОТ'
    return user1, user2


def take_candy(name, b):
    """Сколько конфет возьмет игрок"""
    print('Можно взять от 1 до 28 конфет!')
    if name == 'БОТ':
        a = randint(1, 29)
        print('БОТ берет со стола', a, 'конфет')
    else:
        a = int(
            input(f'{name} Осталось на столе {b} конфет, сколько возьмешь?: '))
    while a < 0 or a > 28:
        a = int(
            input(f'{name} конфет можно взять от 1 до 28! Сколько возьмешь?: '))
    return a


def pritn_result(name, a, b, c):
    """Вывод промежуточных результатов"""
    print(
        f"Ходил {name}, взял {a}, у него {b} конфет. Осталось на столе {c} конфет.")
    print()


def choice_first(user1, user2):
    """Выбират кто первый ходит"""
    print()
    print('Начинаем жеребьевку. Удачи!')
    print()
    num2 = [user1, user2]
    num1 = choice(num2)
    num2.remove(num1)
    print('Первым ходит', num1)
    print()
    return num1, num2


def run_game():
    user1, user2 = user_choice()
    num1, num2 = choice_first(user1, user2)
    candy = 117
    sum_candy_num1 = 0
    sum_candy_num2 = 0
    flag = 1

    while candy > 28:
        if flag == 1:
            a = take_candy(num1, candy)
            candy -= a
            sum_candy_num1 += a
            flag = 2
            pritn_result(num1, a, sum_candy_num1, candy)

        if flag == 2:
            b = take_candy(*num2, candy)
            candy -= b
            sum_candy_num2 += b
            flag = 1
            pritn_result(*num2, b, sum_candy_num2, candy)
    return winner(flag, num1, num2)
    
def winner(flag, num1, num2):
    """Определение победителя"""
    if flag == 1:
        return (f'Победитель {num1}')
    else:
        return (f'Победитель {num2}')



