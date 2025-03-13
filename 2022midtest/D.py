def sum_int_list(input_list, target):
	ans = []
	length = len(input_list)
	for i in range(length):
		aim = target - input_list[i]
		for j in range(i+1, length):
			if input_list[j] == aim:
				ans.append((i,j))
	ans.sort()
	return ans

print(sum_int_list([2, 7, 11, 15], 9),sum_int_list([-3, 3, -4, -8, 7], -1)
, sum_int_list([-3, 3, -4, -8, 7], 1))