#   1. Задайте список. Напишите программу, которая определит,
# присутствует ли в заданном списке  некое число.
# Пример:
# ['114411', 'sjngsjgng', '123fsghs'] -> No
# ['12', 12] -> Yes

l = [123, 'fsfsfs', 'fsf', 'qeq', 3243]
a = "No"
for j in l:
    if str(type(j)) == "<class 'int'>" or type(j) == "<class 'float'>":
        a = 'Yes'
        break
print(a)

# Вариант 2

mass = ['ssss', 'sngujn556', 44]
types = [str(type(i)) for i in mass]
if "<class 'int'>" in types or "<class 'float'>" in types:
    print('Yes')
else:
    print('No')


#   2. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

# Пример:
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

# Вариант 1
l = ["йцу", "фыв", "ячс", "цук", "йцукен", "цук"]


def serch(l, a):
    count = 0
    for i in range(len(l)):
        if l[i] == a:
            count += 1
        if count == 2:
            print(i)
            break
    else:
        print(-1)


serch(l, 'цук')
# Вариант 2
mass = ["123", "234", "123", "567"]
a = "123"
try:
    mass.remove(a)
    print((mass.index(a))+1)
except ValueError:
    print(-1)

# Интересный ввод!

# def input_correct_int():
#     while True:
#         try:
#             return int(input())
#             break
#         except:
#             print('Некорректный ввод')

# a = input_correct_int()
# print(a)
