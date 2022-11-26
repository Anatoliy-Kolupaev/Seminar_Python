# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# *Пример:*
#  Для N = 5: 1, -3, 9, -27, 81
import math
n = int(input('Введите число: '))
for x in range(n):
    print(math.pow(-3, x))

# 2. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# *Пример:*
#  Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = int(input())
a = {}
for i in range(1, n + 1):
    a[i] = 3*i+1
print(a) 

# '3. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.
str1 = input()
str2 = input()
print(str1.count(str2))

# Вариант 2
print(int((len(str1) - len(str1.replace(str2, '')))/len(str2)))

# Вариант 3
count = 0
for i in range(len(str1)):
    if str1[i:i+len(str2)] == str2:
        count += 1
print(count)


