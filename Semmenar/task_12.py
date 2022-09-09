# 3. Напишите программу, которая определит позицию второго
#  вхождения строки в списке либо сообщит, что её нет.
some_list = [input() for _ in range(int(input('Введите кол-во элементов: ')))]
some_str = input('Введите строку: ')
try:
    print(some_list.index(some_str, some_list.index(some_str) + 1))
except:
    print(-1)