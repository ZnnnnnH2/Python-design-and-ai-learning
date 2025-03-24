def num_dates(a):
	length = len(a)
	if length == 0:
		return None
	for k in range(length):
		if type(a[k]) is not int:
			return None

	def helper(i):
		for j in range(i+1,length):
			if a[j] > a[i]:
				return j-i
		return 0

	ans = [helper(0)]

	for i in range(1,length):
		ans.append(helper(i))

	return ans

print(num_dates([]),num_dates(["11", 20]),num_dates([11, 22, 33]),num_dates([1, 2, 4, 3, 2, 5, 3]),num_dates([1, 1, 1, 1, 1]),num_dates([1, 2, 3, 2, 1, 2, 3, 4]))
