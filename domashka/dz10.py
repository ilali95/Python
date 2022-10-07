# Создать класс TrafficLight (светофор):
# ● определить у него один атрибут color (цвет) и метод running (запуск);
# ● атрибут реализовать как приватный;
# ● в рамках метода реализовать переключение светофора в режимы: красный, жёлтый,
# зелёный;
# ● продолжительность первого состояния (красный) составляет 7 секунд, второго
# (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# ● переключение между режимами должно осуществляться только в указанном порядке
# (красный, жёлтый, зелёный);
# ● проверить работу примера, создав экземпляр и вызвав описанный метод.
# import time

# class TrafficLight:
# 	color = 'red'

# 	def running(self):
# 		print(TrafficLight.color)
# 		time.sleep(7)
# 		print('yellow')
# 		time.sleep(5)
# 		print('green')
# 		time.sleep(5)

# t = TrafficLight()
# t.running()

#  Реализовать класс Road (дорога).
# ● определить атрибуты: length (длина), width (ширина);
# ● значения атрибутов должны передаваться при создании экземпляра класса;
# ● атрибуты сделать защищёнными;
# ● определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# ● использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра
# дороги асфальтом, толщиной в 1 см*число см толщины полотна;
# ● проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

class Road:
	def __init__(self, lenght, wight):
		self.lenght = lenght
		self.winght = wight

	def func(self, weight, h):
		return (self.lenght*self.winght*weight*h)/1000

a = Road(20,5000)
print(a.func(25, 5))