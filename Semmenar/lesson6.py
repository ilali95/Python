# class Floodinfo:
# 	def __init__(self, proteins, fats, carbohydrates):
# 		self.proteins = proteins
# 		self.fats = fats
# 		self.carbohydrates = carbohydrates
	
# 	def get_proteins(self):
# 		return self.proteins
	
# 	def get_fats(self):
# 		return self.fats
	
# 	def get_carbohydrates(self):
# 		return self.carbohydrates
	
# 	def get_kcalories(self):
# 		return 4*self.proteins+9*self.fats+4*self.carbohydrates
	
# 	def __add__(self, other):
# 		return Floodinfo(self.proteins + other.proteins, self.fats+other.fats, self.carbohydrates+other.carbohydrates)
	
# food1 = Floodinfo(100, 100, 100)
# food2 = Floodinfo(50,60,70)
# food3 = food1+food2

# print(food1.get_proteins(), food1.get_fats(), food1.get_carbohydrates, food1.get_kcalories())
# print(food2.get_proteins(), food2.get_fats(), food2.get_carbohydrates, food2.get_kcalories())
# print(food3.get_proteins(), food3.get_fats(), food3.get_carbohydrates, food3.get_kcalories())




# class ReversedList:

# 	def __init__(self, some_list):
# 		self.some_list = some_list
	
# 	def __getitem__(self, index):
# 		return self.some_list[-1-index]
	
# 	def __len__(self):
# 		return len(self.some_list)

# r = ReversedList([])
# # for i in range(len(r)):
# print(len(r))

import datetime as dt

class Date:
    def __init__(self, month, day):
        self.month = month
        self.day = day

    def __sub__(self, other):
        day1 = dt.date(2021, self.month, self.day)
        day2 = dt.date(2021, other.month, other.day)
        return str(day2 - day1).split()[0]

day1 = Date(1, 5)
day2 = Date(1, 1)
print(day2 - day1)
