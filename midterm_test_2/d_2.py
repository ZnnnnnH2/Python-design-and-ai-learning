def reverse_words(a):
	ls = a.split(" ")

	def helper(word):
		return word[::-1]

	ans = []
	for word in ls:
		ans.append(helper(word))

	return " ".join(ans)

print(reverse_words('Hello World'),reverse_words('python package'),reverse_words('Renmin University of China'))
#olleH dlroW nohtyp egakcap nimneR ytisrevinU fo anihC