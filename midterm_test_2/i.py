from functools import cmp_to_key


def sorted_with_weird_order(string_list, order):
	hi = "abcdefghijklmnopqrstuvwxyz"
	ord = 0
	dic = {}
	for s in order:
		dic[s] = hi[ord]
		ord += 1

	def cmp(a, b):
		d = {}
		def rep(t):
			if t in d:
				return d[t]
			ans = ""
			for c in t:
				ans += dic[c]
			d[t] = ans
			return ans

		len1 = len(a)
		len2 = len(b)
		min_len = min(len1, len2)
		i = 0
		aa = rep(a)
		bb = rep(b)
		if aa < bb:
			return -1
		elif aa == bb:
			return 0
		else:
			return 1

	string_list.sort(key=cmp_to_key(cmp))
	return string_list


print(sorted_with_weird_order(['c', 'b', 'a'], 'abcdefghijklmnopqrstuvwxyz'))
print(sorted_with_weird_order(['', 'ab', 'a'], 'abcdefghijklmnopqrstuvwxyz'))
print(sorted_with_weird_order(['c', 'b', 'a'], 'acbdefghijklmnopqrstuvwxyz'))
