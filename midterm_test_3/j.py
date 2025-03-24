class Auto(object):
	def __init__(self, brand, color):
		self.__brand = brand
		self.__color = color


class Car(Auto):  # 补全该类
	def __init__(self, brand, color):
		super().__init__(brand, color)

class Bus(Auto):
	def __init__(self, brand, color, carry_passengers):  # 补全该函数，需采用父类构造函数
		super().__init__(brand, color)
		self.carry_passengers = carry_passengers

class AutoMarket(object):
	def __init__(self):
		self.auto = {'Car': [], 'Bus': []}

	def buy_auto(self, auto):  # 补全该函数
		if isinstance(auto, Car):
			self.auto['Car'].append(auto)
		else:
			self.auto['Bus'].append(auto)
	def current_auto_storage(self):  # 补全该函数
		for car in self.auto['Car']:
			print("Having car {0}, color is {1}".format(car._Auto__brand, car._Auto__color))
		for bus in self.auto['Bus']:
			print("Having bus {0}, color is {1}, carry_passengers is {2}".format(bus._Auto__brand, bus._Auto__color,bus.carry_passengers))


def testing_AutoMarket(auto_list):
	# 用于测试，此函数禁止操作，否则记为0分！
	auto_market = AutoMarket()
	for auto in auto_list:
		auto_type = auto[0].split("_")
		if auto_type[0] == "car":
			car = Car(brand=auto[1]['brand'],
					  color=auto[1]['color'])
			auto_market.buy_auto(car)
		elif auto_type[0] == "bus":
			bus = Bus(brand=auto[1]['brand'],
					  color=auto[1]['color'],
					  carry_passengers=auto[1]['carry_passengers']
					  )
			auto_market.buy_auto(bus)
		else:
			print("Incorrect auto type!")
	auto_market.current_auto_storage()


auto_list = [['car_1', {'brand': 'audi_A4', 'color': 'red'}],
			 ['car_2', {'brand': 'xiaomi_su7', 'color': 'blue'}],
			 ['bus_1', {'brand': 'Jinlong', 'color': 'write', 'carry_passengers': 40}],
			 ['car_3', {'brand': 'byd_qin', 'color': 'black'}]]

testing_AutoMarket(auto_list)
