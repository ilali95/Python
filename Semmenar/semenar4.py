# Задача HARD SORT.
# Задайте двумерный массив из целых чисел. Количество строк и столбцов задается с клавиатуры. 
# Отсортировать элементы по возрастанию слева направо и сверху вниз.
# Например, задан массив:
# 1 4 7 2
# 5 9 10 3
# После сортировки
# 1 2 3 4
# 5 7 9 10

# import random

# a = int(input('Строки: '))
# b = int(input('Столбцы: '))

# array_input = []
# for x in range(a):
# 	array_input.append([random.randint(1, 21) for y in range(b)])
# for x in range(a):
# 	print(array_input[x])
# print(array_input)

# lst=[]
# for i in array_input:
# 	lst +=i
# print(sorted(lst))


# import random as r


# def sort(arr):
#     for k in range(len(arr)):
#         min = k
#         for i in range(k, len(arr)):
#             if arr[i] < arr[min]:
#                 min = i
#         arr[min], arr[k] = arr[k], arr[min]

#     return arr


# def median(arr):
#     return arr[(len(arr)) // 2]


# rows = int(input('Число строк в массиве '))
# column = int(input('Число колонок в массиве '))
# matrix = [[r.randint(-10, 10) for i in range(column)] for j in range(rows)]
# temp = []


# def print_dimentional(matrix):
#     for lists in matrix:
#         print(lists)
#     print()


# for i in range(rows):
#     for j in range(column):
#         temp.append(matrix[i][j])

# sorted_temp = sort(temp)

# print()
# print(f'median {median(sorted_temp)}')

# print_dimentional(matrix)

# for i in range(rows):
#     for j in range(column):
#         matrix[i][j] = sorted_temp[i * column + j]

# print_dimentional(matrix)

# # задача 2 HARD необязательная. Сгенерировать массив случайных целых чисел размерностью m*n 
# # (размерность вводим с клавиатуры). Вывести на экран красивенько таблицей. 
# # Перемешать случайным образом элементы массива, причем чтобы каждый гарантированно один раз переместился
# # на другое место и потом не участвовал никак (возможно для этого удобно будет использование множества) 
# # и выполнить это за m*n / 2 итераций. То есть если массив три на четыре, то надо выполнить не более 6 итераций.
# # И далее в конце опять вывести на экран как таблицу.

# from random import randint
# from random import choice

# n = int(input("Insert n: "))
# m = int(input("Insert m: "))

# initList = []
# tempList = []

# for i in range(n):
#     sp = []
#     for j in range(m):
#         sp.append(randint(-10, 10))
#         tempList.append(sp[j])
#     initList.append(sp)
# print(initList)
# print(tempList)
# indexList = [0] * m*n
# for i in range(m*n):
#     indexList[i] = i

# for i in range(int(m*n/2)):
#     a = choice(indexList)
#     indexList.remove(a)
#     b = choice(indexList)
#     indexList.remove(b)
#     tempList[a], tempList[b] = tempList[b], tempList[a]
# resultList = []
# print(tempList)
# for i in range(n):
#     sp = []
#     for j in range(m):
#         sp.append(tempList[0])
#         tempList.remove(tempList[0])
#     resultList.append(sp)

# print(resultList)



# 41. Напишите программу вычисления арифметического выражения заданного строкой. 
# Используйте операции +,-,/,*. приоритет операций стандартный. 
#     *Пример:* 
#     2+2 => 4; 
#     1+2*3 => 7; 
#     1-2*3 => -5;



# - Добавьте возможность использования скобок, меняющих приоритет операций.
# *Пример:* 
# 1+2*3 => 7; 
# (1+2)*3 => 9;


# 43. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# *Пример:* 
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]


# a = [1, 2, 3, 5, 1, 5, 3, 10]
# print(a)
# lst = []
# for i in a:
# 	s=0
# 	for j in a:
# 		if i == j:
# 			s += 1
# 	if s == 1:
# 		lst.append(i)
# print(lst)

# for i in range(len(a)):
# 	for j in range(len(a)):
# 		if i != j and a[i] == a[j]:
# 			break
# 	else:
# 		print(a[i], end=' ')

