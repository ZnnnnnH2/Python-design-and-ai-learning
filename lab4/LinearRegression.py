import torch as t
import torch.nn as nn

class LinearRegression(nn.Module):
	def __init__(self, in_dim):
		super().__init__()
		self.dim = in_dim
		self.w = nn.Parameter(t.randn(self.dim + 1, 1))

	def forward(self, x):
		x = t.cat([x, t.ones((x.shape[0], 1))], dim=1)
		x = x.matmul(self.w)
		return x

def testLRModel(in_dim, data_size = 2):
	layer = LinearRegression(in_dim)
	inputT = t.randn(data_size, in_dim)
	output = layer(inputT)
	print("input: ", inputT)
	print("output: ", output)
	for parameter in layer.parameters():
		print("parameter: ", parameter)

class Linear_Model():
	def __init__(self, in_dim, learing_rate = 0.01, epoches = 10000):
		self.learning_rate = 0.01
		self.epoches = epoches
		self.model = LinearRegression(in_dim)
		self.optimizer = t.optim.SGD(self.model.parameters(), lr=self.learning_rate)
		self.loos_functions = t.nn.MSELoss()

	def train(self, x, y):
		"""
		训练模型
		:param x:  training data matrix
		:param y: 	real output
		:return: 	训练中每一轮的损失值（画图用）
		"""

		losses = []
		for i in range(self.epoches):
			self.optimizer.zero_grad()
			output = self.model(x)
			loss = self.loos_functions(output, y)
			loss.backward()
			self.optimizer.step()
			losses.append(loss.item())
		return losses

	def test(self, x, y):
		"""
		用训练好的模型做测试
		:param x: 测试数据
		:param y: 测试数据的真实标签
		:return: 预测值和精度
		"""
		prediction = self.model(x)
		evaluationMetrics = EvaluationMetrics()
		accuracy = evaluationMetrics.accuracy(y, prediction)
		return prediction, accuracy


	class EvaluationMetrics(object):

		def confusion_matrix(self, y_true, y_pred):
			# 补全该方法
			self.check_size_and_value(y_true, y_pred)

			TP = 0
			FP = 0
			TN = 0
			FN = 0
			length = len(y_true)
			for i in range(length):
				if y_true[i] == 1 and y_pred[i] == 1:
					TP += 1
				elif y_true[i] == 1 and y_pred[i] == 0:
					FN += 1
				elif y_true[i] == 0 and y_pred[i] == 1:
					FP += 1
				elif y_true[i] == 0 and y_pred[i] == 0:
					TN += 1

			return TP, FP, TN, FN

		def accuracy(self, y_true, y_pred):
			# 补全该方法
			self.check_size_and_value(y_true, y_pred)
			TP, FP, TN, FN = self.confusion_matrix(y_true, y_pred)
			return (TP + TN) / (TP + FP + TN + FN)

		# 补全该方法

		def precision(self, y_true, y_pred):
			# 补全该方法
			self.check_size_and_value(y_true, y_pred)
			TP, FP, TN, FN = self.confusion_matrix(y_true, y_pred)
			if TP + FP == 0:
				return 0
			else:
				return TP / (TP + FP)

		def recall(self, y_true, y_pred):
			# 补全该方法
			self.check_size_and_value(y_true, y_pred)
			TP, FP, TN, FN = self.confusion_matrix(y_true, y_pred)
			if TP + FN == 0:
				return 0
			else:
				return TP / (TP + FN)

		def f1(self, y_true, y_pred):
			# 补全该方法
			self.check_size_and_value(y_true, y_pred)
			TP, FP, TN, FN = self.confusion_matrix(y_true, y_pred)
			if TP + FP == 0 or TP + FN == 0:
				return 0
			else:
				return 2 * TP / (2 * TP + FP + FN)

		# 补全该方法

		def check_size_and_value(self, y_true, y_pred):
			if y_true.shape != y_pred.shape:
				raise ValueError("y_true and y_pred must have the same shape")
			if not np.all(np.isin(y_true, [0, 1])):
				raise ValueError("y_true must only contain 0s and 1s")
			if not np.all(np.isin(y_pred, [0, 1])):
				raise ValueError("y_pred must only contain 0s and 1s")




