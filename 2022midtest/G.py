def valid_string(string, dictionary):
	d = list(dictionary)
	sset = set()
	for i in d:
		sset.add(len(i))
	cd = list(sset)
	length = len(string)
	le = len(cd)
	i = 0
	ok = set()
	nook = set()
	def helper(i):
		if i in ok:
			return True
		if i in nook:
			return False
		if i >= length:
			return True
		for j in range(le):
			if i + cd[j] <= length and string[i:i + cd[j]] in d:
				if helper(i + cd[j]):
					ok.add(i)
					return True
		nook.add(i)
		return False

	return helper(i)


print(valid_string("abcabc", {"a", "b", "c"}))
print(valid_string("abcabd", {"a", "b", "c"}))
print(valid_string("aabbcc", {"aa", "bb", "ccc"}))
print(valid_string("", {"aa", "bb", "ccc"}))
