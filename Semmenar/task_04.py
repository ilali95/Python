# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
    
#     *Примеры:*
    
#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3

# Решение 1


number=float(input('Введите число: '))
num=(number*10)%10
if num==0:
	print('Нет')
else:
	print(int(num))

	
# Решение 2
number = float(input())
if number // 1 == number:
    print('нет')
else:
    print(int((number * 10 % 10)))
