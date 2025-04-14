from collections import defaultdict

def a(ls):
	str1 = "abcdefghijklmnopqrstuvwxyz"
	base = 1
	dd = defaultdict(lambda: 0)
	for i in ls:
		dd[i] += base
		base+=1
	for i in ls:
		for x in i:
			dd[x] -= 100
	ls.sort(key = lambda s:[dd[x] for x in s])
	return ls

print(a(["","ab","b"]))