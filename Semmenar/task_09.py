from datetime import datetime


# 1. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора 
# псевдослучайных чисел.
x = 15
y = 5

d = str(datetime.now())
res = ""
for i in d:
    if i.isdigit():
        res += i
t = int(res) % (y-x)+x
print(t)

# 2. Задайте список. Напишите программу, которая определит, присутствует 
# ли в заданном списке строк некое число.
# list_int = ["22", "23", "7589","214"]
# n = input("Введите N: ")
# for i in list_int:
#     if n == i:
#         print("Есть")
#         break
# else:
#     print("Нет")   

# 3. Напишите программу, которая определит позицию второго вхождения строки 
# в списке либо сообщит, что её нет.
# list_str = ["йцу", "фыв", "ячс", "цук","йцу", "йцукен", "выа", "qrqc"]
# str1 = input("Введите строку:")
# count_ = 0

# for i in range(0,len(list_str)):
#     if str1 == list_str[i]:
#         count_ += 1
#     if count_ == 2:
#         print(i)
#         break
# else:
#     print(-1)

        
# print(list_str.index(str1, list_str.index(str1) + 1, -1))
