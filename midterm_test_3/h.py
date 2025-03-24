from collections import defaultdict
def count_characters(string):
	string = string.lower()
	dic = defaultdict(lambda :0)
	for c in string:
		dic[c] += 1
	ls = list(dic.items())
	ls.sort(key=lambda x:x[0])
	length = len(ls)
	ans = ""
	for i in range(length-1):
		ans +=f"{ls[i][0]}:{ls[i][1]}, "
	ans+=f"{ls[length-1][0]}:{ls[length-1][1]}"
	return ans

count_characters("AAAbb")