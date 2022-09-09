# 1. Реализуйте алгоритм задания случайных чисел без
# использования встроенного генератора псевдослучайных чисел.
import time

print(str(time.time()).split(".")[-1])
a = int(str(time.time()).split(".")[-1])
start = int(input())
end = int(input())
print(a % (end + 1 - start) + start)
