def count_sum_int_float(input_list):
	length = len(input_list)
	if length == 0:
		return 0, None
	tot = 0
	ans = 0
	for i in input_list:
		if type(i) == int:
			tot += 1
			ans += i
		elif type(i) == float:
			tot += 1
			ans += i
	if tot == 0:
		return 0, None
	return tot, ans


print(count_sum_int_float([2, "f", 5]),
	  count_sum_int_float(["a", "b"]),
	  count_sum_int_float([(1, 2), 1, 2, [1, 2]]))
