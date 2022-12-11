# Задача 1
# Вводятся названия городов в одну строчку через запятую. Необходимо определить функцию map,
# которая бы возвращала названия городов только длиной более 5 символов. Вместо остальных названий -
# строку с дефисом ("-").
# Сформировать список из полученных значений и отобразить его на экране в одну строчку через запятую.
# Ввод:
# Москва,Уфа,Вологда,Тула,Владивосток,Хабаровск
# Вывод:
# Москва,-,Вологда,-,Владивосток,Хабаровск

l = 'Москва,Уфа,Вологда,Тула,Владивосток,Хабаровск'
b = ','.join(i if len(i) > 5 else '-' for i in l.split(','))
print(b)

# 2 Вариант с мар()

c = map(lambda x: x if len(x) > 5 else '-', l.split(','))
print(','.join(c))

# Задача 2.
# На вход программы поступает строка в формате:
# ключ_1=значение_1 ключ_2=значение_2 ... ключ_N=значение_N
# Необходимо с помощью функции map преобразовать ее в кортеж tp вида:
# tp = (('ключ_1', 'значение_1'), ('ключ_2', 'значение_2'), ..., ('ключ_N', 'значение_N'))
# Ввод:
# house=дом car=машина men=человек tree=дерево
# Вывод:
# (('house', 'дом'), ('car', 'машина'), ('men', 'человек'), ('tree', 'дерево'))

s = 'house=дом car=машина men=человек tree=дерево'.split()
n = tuple(map(lambda x: tuple(x.split('=')), s))
print(n)