# 1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#   Пример:
# - 6782 -> 23
# - 0,56 -> 11

# n = input("Введите число: ")
# suma = 0
# for i in n:
#     if i.isdigit():
#         suma += int(i)
# print(f"{n} -> {suma}")

# 2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#   Пример:
#   пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# n = int(input("Введите число: "))
# count = 1
# lst=[]
# for i in range(1, n+1):
# 	count*=i
# 	lst.append(count)

# print(f'N = {n}, тогда {lst}')

# 3 Задайте список из n чисел последовательности $(1+\frac 1 n)^n$
#   и выведите на экран их сумму.


# def func(x):
#     return (1 + 1 / x) ** x

# some_dict = []
# n = int(input("Введите число: "))

# for i in range(1, n + 1):
#     some_dict.append(func(i))
# print(some_dict)
# res = sum(some_dict)
# print(round(res, 2))


# some_dict = {}
# n = int(input("Введите число: "))

# for i in range(1, n + 1):
#     some_dict[i] = func(i)
# res = sum(some_dict.values())
# print(round(res, 2))


# 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#   Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

import random

n = int(input("Введите число: "))
lst = []

for i in range(n):
    lst.append(random.randint(-n, n))
print(lst)

m = open("file.txt", "w")
len_m = random.randint(1, n)
for i in range(len_m):
	m.write(str(random.randint(1, n-1)))
	m.write('\n')
m.close()

sum = 1
f = open('file.txt', 'r')
for i in range(len_m):
	sum *= lst[int(f.readline())]

print(sum)

# 5 Реализуйте алгоритм перемешивания списка.
# import random

# lst = [str(i) for i in input('Введите значения списка через пробел: ').split()]
# print(f'Начальный список {lst}')
# random.shuffle(lst)
# print(f'Перемешаный список {lst}')
