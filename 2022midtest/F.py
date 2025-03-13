def string_sorting(string_list):
	co = []
	length_string_list = len(string_list)
	sset = set()
	ans = []
	for i in range(length_string_list):
		if type(string_list[i]) == str:
			co.append(string_list[i])
		else:
			sset.add(i)
	i,j=0,0
	co.sort()
	while i<length_string_list and j<length_string_list:
		if i in sset:
			ans.append(string_list[i])
		else:
			ans.append(co[j])
			j+=1
		i+=1
	return ans

print(string_sorting([2.9, "world", "hello"]), string_sorting(["world", 2, "hello"]),string_sorting([1, 3, 2]))

print(string_sorting([]))