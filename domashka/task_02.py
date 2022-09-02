# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# Решение 1
# list = []
# for i in range(3):
#     number = int(input("Введите число: "))
#     list.append(number)
# print(list)
# mas1 = not (list[0] or list[1] or list[2])
# mas2 = not list[0] and not list[1] and not list[2]
# if mas1 == mas2:
#     print("Истина")
# else:
#     print("Ложно")

# Решение 2
for x in range(2):
    for y in range(2):
        for z in range(2):
            if not (x or y or z) == (not (x) and not (y) and not (z)):
                print(f'{x}, {y}, {z}, {True}')
            else:
                print(f'{x}, {y}, {z}, {False}')
