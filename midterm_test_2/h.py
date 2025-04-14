import collections


def word_cut(string, dictionary):
	if string == "":
		return [], 0
	length = len(string)
	dic_set = set(dictionary.keys())
	len_set = set([len(x) for x in dictionary.keys()])
	len_ls = list(len_set)
	ans = collections.defaultdict(lambda: 0)
	ans_cut = collections.defaultdict(lambda: list())

	def helper(index):
		if index >= length:
			return
		for leng in len_ls:
			s = string[index:index + leng]
			if s in dic_set:
				# ans[index+leng] = max(ans[index+leng],ans[index]+dictionary[s])
				if ans[index + leng] <= ans[index] + dictionary[s]:
					ans[index + leng] = ans[index] + dictionary[s]
					ans_cut[index + leng] = ans_cut[index].copy()
					ans_cut[index + leng].append(s)
				helper(index + leng)

	helper(0)
	if ans[length] == 0:
		return None, ans_cut[length]
	return ans_cut[length], ans[length]


print(word_cut("abcabc", {"a": 1, "b": 1, "c": 1}))
print(word_cut("abcabd", {"a": 1, "b": 1, "c": 1}))
print(word_cut("南京市长江大桥",
			   {"南京": 10, "南京市": 12, "市长": 10, "长江": 10, "大桥": 10, "长江大桥": 25, "江大桥": 1}))
print(word_cut("中华人民共和国", {"中华": 1, "人民": 1, "共和国": 1, "中华人民": 1, "中华人民共和国": 1}))
print(word_cut("中华人民共和国", {"中华": 10, "人民": 10, "共和国": 15, "中华人民": 22, "中华人民共和国": 100}))
print(word_cut("", {"南京": 10, "南京市": 12, "市长": 10, "长江": 10, "大桥": 10, "长江大桥": 25, "江大桥": 1}))
print(word_cut("abcd", {"abc": 100000, "ab": 1, "cd": 1}))
