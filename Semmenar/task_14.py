
# products = ['iPad', 'Samsung Galaxy', 'iPhone', 'iRiver']
# lst = list(filter(lambda x: x[0] == 'i', products))
# print(lst)


# ЗАДАЧА. Есть список с ценами на товары (тип данных — str ), получить из него
# кортеж с ценами (тип данных — float )

# prices = ['1578.4', '892.4', '354.1', '871.5']
# lst = tuple(map(float, prices))
# print(lst)

# ЗАДАЧА
# применить скидку к товарам и округлить до 2 знака


# DISCOUNT = 7
# prices = ['1578.4', '892.4', '354.1', '871.5']
# array = list(map(lambda x: round(float(x)*0.07, 2), prices))
# print(array)


str = input('Enter string: ').replace('абв', '').split(' ')
result = ' '.join(list(filter(lambda x: x != '', str)))
print(result)
