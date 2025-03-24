def max_in_list(data):
	max_mun = -0x3f3f3f3f
	for i in data:
		if type(i) is int or type(i) is float:
			if i > max_mun:
				max_mun = i
		elif type(i) is tuple or type(i) is list or type(i) is set:
			t = max_in_list(i)
			if t is not None:
				if t > max_mun:
					max_mun = t
	if max_mun != -0x3f3f3f3f:
		return max_mun
	return None

print(max_in_list([10,-0.2]),max_in_list(["15.5", 7, [(9,2),-2]]),max_in_list(['a',('b','c')]),max_in_list([5, {16, 2}]))