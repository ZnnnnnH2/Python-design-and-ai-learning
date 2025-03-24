def reverse_even_characters(string):
	string = " "+string
	ls = []
	l = 1
	r = len(string)-1
	if r%2 == 1:
		r -= 1
	length = len(string)
	while l<length and r>=1:
		ls.append(string[l])
		ls.append(string[r])
		r -= 2
		l+=2
	if l<length:
		ls.append(string[l])
	return ''.join(ls)

print(reverse_even_characters("a1b2c3d"))