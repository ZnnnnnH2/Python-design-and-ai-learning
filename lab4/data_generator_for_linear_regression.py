import random as r
import torch as t
class Generator:
	def __init__(self, in_dim, data_size, func, begin = -1, end = 1):
		self.in_dim = in_dim
		self.data_size = data_size
		self.func = func
		self.begin = begin
		self.end = end

	def generate(self, seed):
		"""
		生成数据
		:return: 训练数据和测试数据
		"""
		x = []
		y = []
		r.seed(seed)
		for i in range(self.data_size):
			x.append([r.uniform(self.begin, self.end) for _ in range(self.in_dim)])
			y.append([self.func(x[i][0])])
		x = t.tensor(x)
		y = t.tensor(y)
		# print("x: ",x)
		# print("y: ",y)
		return x, y

	def __call__(self, seed):
		return self.generate(seed)
