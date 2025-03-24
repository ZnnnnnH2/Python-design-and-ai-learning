def sorted_with_weird_order(string_list, order):
	s0 = "abcdefghijklmnopqrstuvwxyz"
	dic_to = {}
	dic_back = {}
	mun = 0
	for s in order:
		dic_to[s] = s0[mun]
		dic_back[s0[mun]] = s
		mun += 1

	def change(s,dic):
		ans = ""
		for c in s:
			ans += dic[c]
		return ans

	ls1 = []
	for s in string_list:
		ls1.append(change(s,dic_to))
	ls1.sort()
	ans_final = []
	for s in ls1:
		ans_final.append(change(s,dic_back))
	return ans_final

print(sorted_with_weird_order(['c', 'b', 'a'], 'abcdefghijklmnopqrstuvwxyz'))
print(sorted_with_weird_order(['', 'ab', 'a'], 'abcdefghijklmnopqrstuvwxyz'))
print(sorted_with_weird_order(['c', 'b', 'a'], 'acbdefghijklmnopqrstuvwxyz'))
