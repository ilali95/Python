# def some_function(x):
#     return x * 2
#
#
# lambda_function = lambda x: x * 2
#
# print(some_function(5))
# print(lambda_function(5))


# f1 = lambda: 10 + 20
# f2 = lambda х, у: х + у
# f3 = lambda х, у, z: х + у + z
#
# print(f1())
# print(f2(5, 10))
# print(f3(5, 10, 30))

def compare_by_second(point):
    return point[1]


def compare_by_sum(point):
    return point[0] + point[1]


points = [(1, -1), (2, 3), (-10, 15), (10, 9), (7, 18), (1, 5), (2, -4)]

print(sorted(points, key=compare_by_second))
print(sorted(points, key=compare_by_sum))
print('---')
print(sorted(points, key=lambda point: point[1]))
print(sorted(points, key=lambda point: point[0] + point[1]))


