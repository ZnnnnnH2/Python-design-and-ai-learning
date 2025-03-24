
class Student:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def display(self):
		print("Name:", self.name)
		print("Age:", self.age)

	def add(self, k):
		self.age = self.age + k

s = Student
s1 = s("John", 22)
s1.display()
s1.func = lambda self,x: self.add(x)
s1.func(s1,3)
s1.display()



