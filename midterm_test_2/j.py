class Animal(object):
	def __init__(self, name):
		self.__name = name

	def speak(self):
		print("I am an animal.")

	def get_name(self):
		return self.__name

class Dog(Animal):
	def __init__(self, name):
		super(Dog, self).__init__(name)
		self.__species = 'Dog'

	def speak(self):
		print("I am a Dog.")

	def play(self):
		print(f"Dog {super().get_name()} is playing.")

	def get_species(self):
		return self.__species


class Cat(Animal):
	def __init__(self, name):
		super(Cat, self).__init__(name)
		self.__species = 'Cat'

	def speak(self):
		print("I am a Cat.")

	def play(self):
		print(f"Cat {super().get_name()} is playing.")

	def get_species(self):
		return self.__species


class PetShop(object):
	def __init__(self):
		self.__PatShop = []

	def add_pet(self, pet):
		self.__PatShop.append((pet.get_species(), pet.get_name()))

	def show_pets(self):
		for pet in self.__PatShop:
			print(f"{pet[1]} is {pet[0]}.")


def testing_PetShop(pet_dict):
	pet_shop = PetShop()
	for species, name in pet_dict.items():
		species = species.split("_")
		if species[0] == "Dog":
			dog = Dog(name)
			dog.speak()
			dog.play()
			pet_shop.add_pet(dog)
		elif species[0] == "Cat":
			cat = Cat(name)
			cat.speak()
			cat.play()
			pet_shop.add_pet(cat)
		else:
			print("Incorrect dict keys!")
	pet_shop.show_pets()


testing_PetShop({"Dog_1": "Tom", "Dog_2": "Bob", "Cat": "Lucy"})
