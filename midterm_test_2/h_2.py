import collections
from collections import deque,defaultdict


def word_cut(string, dictionary):
	if string == "":
		return [],0
	d = list(dictionary)
	sset = set()
	for i in d:
		sset.add(len(i))
	cd = list(sset)
	length = len(string)
	le = len(cd)
	ok = defaultdict(lambda : -1)
	nook = set()
	ans = defaultdict(lambda : deque())
	def helper(i):
		if ok[i] != -1:
			return ok[i]
		if i in nook:
			return -1
		if i >= length:
			return -1
		for j in range(le):
			if i + cd[j] <= length and string[i:i + cd[j]] in d:
				if i+cd[j] == length:
					if ok[i] < dictionary[string[i:i + cd[j]]]:
						ok[i] = dictionary[string[i:i + cd[j]]]
						ans[i].clear()
						ans[i].append(string[i:i + cd[j]])
				t = helper(i + cd[j])
				if t != -1 :
					if ok[i] < t+dictionary[string[i:i + cd[j]]]:
						ok[i] = t+dictionary[string[i:i + cd[j]]]
						ans[i]=ans[i+cd[j]].copy()
						ans[i].appendleft(string[i:i + cd[j]])
		if ok[i] != -1:
			return ok[i]
		else:
			nook.add(i)
			return -1

	t = helper(0)
	if t != -1:
		return list(ans[0]),t
	else:
		return None,0

print(word_cut("abcabc", {"a": 1, "b": 1, "c": 1}))
print(word_cut("abcabd", {"a": 1, "b": 1, "c": 1}))
print(word_cut("南京市长江大桥", {"南京": 10, "南京市": 12, "市长": 10, "长江": 10, "大桥": 10, "长江大桥": 25, "江大桥": 1}))
print(word_cut("中华人民共和国", {"中华": 1, "人民": 1, "共和国": 1, "中华人民": 1, "中华人民共和国": 1}))
print(word_cut("中华人民共和国", {"中华": 10, "人民": 10, "共和国": 15, "中华人民": 22, "中华人民共和国": 100}))
print(word_cut("",{"南京": 10, "南京市": 12, "市长": 10, "长江": 10, "大桥": 10, "长江大桥": 25, "江大桥": 1}))
print(word_cut("abcd",{"abc":100000,"ab":1,"cd":1}))