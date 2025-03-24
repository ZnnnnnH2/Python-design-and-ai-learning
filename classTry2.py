from typing_extensions import override


class person:
	totMun = 0

	def __init__(self, name, age):
		self.__name = name
		self.__age = age
		person.totMun += 1

	def printf(self):
		print(self.__name)
		print(self.__age)


class student(person):

	@override
	def __init__(self, name, age, marks):
		super().__init__(name, age)
		self.__marks = marks

	@override
	def printf(self):
		person.printf(self)
		print(self.__marks)


s = student("Alice", 13, 100)
s.printf()
print(dir(s))
