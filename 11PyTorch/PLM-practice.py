from cmath import log
from math import exp

import matplotlib.pyplot as plt
import torch as t
import torch.nn as nn

from lab4.data_generator_for_linear_regression import Generator


class LinearRegression(nn.Module):
	def __init__(self, in_dim, hidden_dim1, hidden_dim2):
		super().__init__()
		self.first_layer = nn.Linear(in_dim, hidden_dim1)
		self.second_layer = nn.Linear(hidden_dim1, hidden_dim2)
		self.third_layer = nn.Linear(hidden_dim2, 1)
		self.sigmoid = nn.Sigmoid()

	def forward(self, x):
		hidden_out1 = self.first_layer(x)
		hidden_out2 = self.second_layer(hidden_out1)
		output = self.third_layer(hidden_out2)
		return output

class MLP:
	def __init__(self, in_dim, hidden_dim1, hidden_dim2, learning_rate=0.01, epoches=10000):
		self.learning_rate = learning_rate
		self.epoches = epoches
		self.model = LinearRegression(in_dim, hidden_dim1, hidden_dim2)
		self.optimizer = t.optim.SGD(self.model.parameters(), lr=self.learning_rate)
		self.loss_function = nn.MSELoss() #using BCEloss in logistics regression

	def train(self, x, y):
		losses = []
		for i in range(self.epoches):
			self.optimizer.zero_grad()
			output = self.model(x)
			loss = self.loss_function(output, y)
			loss.backward()
			self.optimizer.step()
			losses.append(loss.item())# turn tensor to a number
		return losses

	def test(self, x, y):
		prediction = self.model(x)
		loss = self.loss_function(prediction, y)
		return prediction, loss

def creat_data(in_dim, data_size, func, begin=-1, end=1):
	"""
	生成数据
	:return: 训练数据和测试数据
	"""
	generator = Generator(in_dim, data_size, func, begin, end)
	xx, yy = generator(114514)
	xx = xx.clone().detach().requires_grad_(True)
	yy = yy.clone().detach().requires_grad_(True)
	return xx, yy

def draw_loss(losses):
	"""
	画损失函数
	:return:
	"""
	plt.figure()
	plt.plot(losses)
	plt.xlabel("epoches")
	plt.ylabel("loss")
	plt.title("loss function")
	plt.show()

def draw_x_y_predicted_y(model, x, y):
	"""
	画图
	:param x: 训练数据
	:param y: 真实标签
	:param predicted_y: 预测标签
	:return:
	"""
	predicted_y = model.test(x, y)
	plt.scatter(x[:,0], y, color='blue')
	plt.scatter(x[:,0], predicted_y[0], color='red')
	plt.xlabel("x1")
	plt.ylabel("x2")
	plt.title("x and y")
	plt.show()

if __name__ == '__main__':
	in_dim = 1
	hidden_dim1 = 2
	hidden_dim2 = 2
	learning_rate = 0.01
	epoches = 10000

	# 生成数据
	func = lambda tt: tt*3+2
	data_size = 1000
	begin = 1
	end = 10
	x, y = creat_data(in_dim, data_size, func, begin, end)
	print("x: ", x)
	print("y: ", y)
	# 训练模型
	mlp = MLP(in_dim, hidden_dim1, hidden_dim2, learning_rate, epoches)
	losses = mlp.train(x, y)
	draw_loss(losses)
	# 测试模型
	draw_x_y_predicted_y(mlp, x, y)