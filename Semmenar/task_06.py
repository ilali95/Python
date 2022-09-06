# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
#*Пример:*
# - Для N = 5: 1, -3, 9, -27, 81


# n = int(input())
# string = ""
# for i in range(0, n-1):
#     string += str((-3) ** i) + ", "
# string += str(-(-3 ** (n - 1)))
# print(string)

# dict= {}
# for i in range(1,n+1):
# 	dict[i]=3*i+1
# print (dict)

n = int(input())
some_list = []
for i in range(n):
    some_list.append((-3) ** i)
print(*some_list, sep=', ')
