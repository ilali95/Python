class Auto:
	def __init__(self):
		print("Автомобиль заведен")
		self.auto_name = "Mazda"
		self._auto_year = 2019
		self.__auto_model = "CX9"

a = Auto()
print(a.auto_name)
print(a.auto_year)
print(a.auto_model)