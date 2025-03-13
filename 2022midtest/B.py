def list_median(input_list):
	length = len(input_list)
	if length == 0:
		return None
	input_list.sort()
	if length % 2 == 1:
		return input_list[length // 2]
	else:
		return (input_list[length // 2] + input_list[length // 2 - 1]) / 2


print(list_median([3, 2, 5]))
print(list_median([2, 5, 3, 4]))
print(list_median([]))