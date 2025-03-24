from collections import defaultdict
def find_letter(a):
	dic = defaultdict(lambda :0)
	length = len(a)
	for i in range(length):
		dic[a[i]] += 1
	for i in range(length):
		if dic[a[i]] == 1:
			return i,a[i]
	return None