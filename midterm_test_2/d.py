def reverse_words(a):
	ls = a.split(" ")

	def helper(word):
		s = ""
		length = len(word)
		for i in range(length-1,-1,-1):
			s+=word[i]
		return s

	ans = ""
	for i in ls:
		ans+=helper(i)
		ans+=" "

	return ans[0:-1]

print(reverse_words('Hello World'),reverse_words('python package'),reverse_words('Renmin University of China'))