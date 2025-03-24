def min_in_list_2(data):
	min1 = 0x3f3f3f3f
	min2 = 0x3f3f3f3f
	index1 = -1
	index2 = -1
	length = len(data)
	for i in range(length):
		if type(data[i]) is str:
			continue
		if data[i] < min1:
			min2,min1 = min1,data[i]
			index2,index1 = index1,i
		elif data[i] >= min1:
			if data[i] < min2:
				min2 = data[i]
				index2 = i
	if index2 == -1:
		return None
	return min2, index2

print(min_in_list_2([10,-0.2]),min_in_list_2(["15.5", 7, 9, 2, -2, 2]),min_in_list_2(['a','b','c']),min_in_list_2([5, 2, 2]))