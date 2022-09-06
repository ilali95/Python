# 2. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# *Пример:*
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# n = int(input())
# some_dict = {}
# for i in range(1, n + 1):
#     some_dict[i] = 3 * i + 1
# print(some_dict)

def func(x):
    return 3 * x + 1

n = int(input())
some_dict = {}
for i in range(1, n + 1):
    some_dict[i] = func(i)
print(some_dict)
