# 1. Задайте строку из набора чисел. Напишите программу, которая
# покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.


# lst=[int (i) for i in input('Введите значения списка через пробел: ').split()]
# print(f'max = {max(lst)}, min = {min(lst)}')


# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
#     1) с помощью математических формул нахождения корней квадратного уравнения
#     2) с помощью дополнительных библиотек Python

# import sympy as sp
# a=int(input('Ведите число: '))
# b=int(input('Ведите число: '))
# c=int(input('Ведите число: '))

# x = sp.Symbol('x')
# s = sp.solveset(a*x**2+b*x+c, x)

# print(s)

# import math

# print("Ax² + Bx + C = 0:")
# a = float(input("a = "))
# b = float(input("b = "))
# c = float(input("c = "))

# discr = b ** 2 - 4 * a * c
# print("Дискриминант D = %.2f" % discr)

# if discr > 0:
#     x1 = (-b + math.sqrt(discr)) / (2 * a)
#     x2 = (-b - math.sqrt(discr)) / (2 * a)
#     print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
# elif discr == 0:
#     x = -b / (2 * a)
#     print("x = %.2f" % x)
# else:
#     print("Корней нет")


# 3. Задайте два числа. Напишите программу, которая найдёт НОК
#  (наименьшее общее кратное) этих двух чисел.

# import math

# a=int(input('Ведите число: '))
# b=int(input('Ведите число: '))
# print(math.lcm(a,b))

# 1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
# Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию,
# необходимую для перевода: какой тип данных выбрать, в теле функции или снаружи.
# 2. * (вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с числительными,
#  начинающимися с заглавной буквы — результат тоже должен быть с заглавной. Например:
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"


def num_translate(k):
	d = {'one': 'один', 'two': 'два','three': 'три','four':'четыре', 'five': 'пять','six': 'шесть','seven': 'семь', 'eight':'восемь','nine':'девять','ten': 'десять'}
	if k.islower():
		return d.get(k)
	else:
		return d.get(k.lower()).title()

num = input("Ведите число: ")
print(num_translate(num))

# lst = [(i, i**2) for i in range(1, 21) if not i%2]
# print(lst)