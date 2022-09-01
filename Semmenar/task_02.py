# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
    
#     Примеры:
    
#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90


# Решение 1
# some_list = []
# for i in range(5):
#     number = int(input('Введите число: '))
#     some_list.append(number)
	
# maxx = some_list[0]
# for j in some_list:
#     if j > maxx:
#         maxx = j
# print(maxx)


# Решение 2
# maxx = int(input('Введите число'))
# for i in range(4):
#     number = int(input('Введите число: '))
#     if number > maxx:
#         maxx = number

# print(maxx)


# Решение 3
some_list =[]
for o in range(5):
	number=int(input('Введите число: '))
	some_list.append(number)

print(max(some_list))