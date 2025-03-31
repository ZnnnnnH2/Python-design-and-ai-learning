
class Student:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def display(self):
		print("Name:", self.name)
		print("Age:", self.age)

	def add(self, k):
		self.age = self.age + k

	def print_all(self):
		for key,value in self.__dict__.items():
			print(key, value)

s = Student
s1 = s("John", 22)
s1.display()
s1.func = lambda self,x: self.add(x)
s1.func(s1,3)
s1.display()
print()
s1.print_all()




