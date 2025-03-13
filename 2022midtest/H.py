from matplotlib.pyplot import inferno


class Counting(object):

	def __init__(self, input_data):
		self.data = input_data
		self.input_data = input_data
		self.s = {}

	def counting(self):
		for i in self.input_data:
			if i not in self.s:
				self.s[i] = 1
			else:
				self.s[i] += 1
		return self.s



# 补全该函数

class CountingMore(Counting):

	def __init__(self, input_data):
		super(CountingMore, self).__init__(input_data)

	# 补全该函数

	def counting_maxkey(self):
		maxx = -0x3f3f3f3f
		for i in self.input_data:
			if i>maxx:
				maxx = i
		return self.s[maxx]

def counting_list(data):
	countingObject = CountingMore(data)  # CountingMore类实例化
	all_key_counting = countingObject.counting()  # 调用子类继承自父类的方法counting()
	max_key = countingObject.counting_maxkey()  # 调用子类的方法counting_maxkey()

	return [all_key_counting, max_key]

print(counting_list([1,2,3,4,5,5.1]))
print(counting_list([4]))
print(counting_list([5,5,5,5.2,5.0]))