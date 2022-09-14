# 1 Задайте список из нескольких чисел. Напишите программу, которая 
#  найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


# lst=[int (i) for i in input('Введите значения списка через пробел: ').split()]
# lst1=[]
# for i in range(0, len(lst)):
# 	if i%2 == 1:
# 		lst1.append(lst[i])
# s = sum(lst1)
# print(f'{lst} -> {lst1} = {s}')


# # 2 Напишите программу, которая найдёт произведение пар чисел списка. 
# # Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# # Пример:
# # - [2, 3, 4, 5, 6] => [12, 15, 16];
# # - [2, 3, 5, 6] => [12, 15]


# lst=[int (i) for i in input('Введите значения списка через пробел: ').split()]
# lst1=[]
# lst1.extend(lst)
# lst2=[]
# for i in lst:
# 	lst2.append(lst[0]*lst[-1])
# 	lst.pop(0)
# 	lst.pop(-1)
# if len(lst)==1:
# 	lst2.append(lst[0]*lst[0])
# print(f'{lst1} -> {lst2}')


# 3 Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


# lst=[float (i) for i in input('Введите значения списка через пробел: ').split()]
# lst1=[]

# for i in range(0, len(lst)):
# 	lst1.append(lst[i]%1)
# max_num=max(lst1)
# min_num=min(lst1)
# res=max_num - min_num
# s = int(res * 100) / 100
# print(f'{lst} -> {s}')


# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


# n = int(input('Введите число: '))
# a = n
# b = ''
# while n > 0:
#     b = str(n % 2) + b
#     n = n // 2
# print(f'{a} -> {b}')


# 5 Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.


# def fib1(n):
# 	fib1 = 0
# 	fib2 = 1
# 	for i in range(0, n):
# 		fib1, fib2 = fib2, fib1 + fib2
# 	return fib2

# def fib2(n):
# 	fib1 = 0
# 	fib2 = 1
# 	for i in range(0, n):
# 		fib1, fib2 = fib2, fib1 +(-fib2)
# 	return fib2

# lst1=[0, ]
# n = int(input('Fibonacci = '))
# for i in range(n):
# 	lst1.append(fib1(i))

# lst2=[ ]
# for i in range(n):
# 	lst2.append(fib2(i))
# 	lst3=lst2[::-1]

# res = lst3+lst1
# print(res)

# k = int(input("Inset k: "))
#
# fibonacciList = [0]*(k*2+1)
# print(fibonacciList)
# fibonacciList[k] = 0
# fibonacciList[k+1] = 1
#
# for i in range(k+2, len(fibonacciList)):
#     fibonacciList[i] = fibonacciList[i-2]+fibonacciList[i-1]
#
# for i in range(k, -1, -1):
#     fibonacciList[i] = fibonacciList[i+2]-fibonacciList[i+1]
#
# print(fibonacciList)
