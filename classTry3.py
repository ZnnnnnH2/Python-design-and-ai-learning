class student:
	def __init__(self, name, age, marks):
		self.__name = name
		self.__age = age
		self.__marks = marks

	def printf(self):
		print(self.__name)
		print(self.__age)
		print(self.__marks)


s = list()

d = dict()

print(s.__class__)
print(d.__class__)

s.__class__ = student
d[3] = 4
print(d.items())