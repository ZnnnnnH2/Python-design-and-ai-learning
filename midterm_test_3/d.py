def elementwise_product(x, y):
	if isinstance(x, int) and isinstance(y, int):
		return x * y
	ans = []
	length = len(x)
	for i in range(length):
		ans.append(elementwise_product(x[i], y[i]))
	return ans

x, y = [1,2,3], [1,2,3]
print(elementwise_product(x, y))

x, y = [[1,2,3], [2,3,1], [3, 1, 2]], [[1,0,0], [0,1,0], [0,0,1]]
print(elementwise_product(x, y))