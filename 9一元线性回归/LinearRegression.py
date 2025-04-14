from sys import pycache_prefix

import numpy as np


class LinearRegression:

	def __init__(self, learning_rate=0.01, max_iterations=1000, seed=None):
		np.random.seed(seed)
		self.lr = learning_rate
		self.max_iterations = max_iterations
		self.w = np.random.normal(1, 0.1)
		self.b = np.random.normal(1, 0.1)
		self.loss_arr = []

	def predict(self, x):
		return self.__f(x, self.w, self.b)

	def __f(self, x, w, b):
		return x * w + b

	def loss(self, y_true, y_pred):
		return np.mean((y_true - y_pred) ** 2)

	def fit(self, x, y):
		for i in range(self.max_iterations):
			self.__train(x, y)
			y_pred = self.predict(x)
			self.loss_arr.append(self.loss(y, y_pred))

	def __train(self, x, y):
		dw, db = self.__calc_gradient(x, y)
		self.w = self.w - self.lr * dw
		self.b = self.b - self.lr * db
		return self.w, self.b

	def __calc_gradient(self, x, y):
		dw = np.mean(2 * (self.w * x + self.b - y) * x)
		db = np.mean(2 * (self.w * x + self.b - y))
		return dw, db


if __name__ == '__main__':
	import matplotlib.pyplot as plt

	np.random.seed(114514)
	data_size = 100
	x = np.random.uniform(1, 10, data_size)
	y = x * 20 + 10 + np.random.normal(0, 10, data_size)


	regr = LinearRegression(learning_rate=0.01, max_iterations=1000, seed = 13454234)
	regr.fit(x, y)

	print(regr.w, regr.b)