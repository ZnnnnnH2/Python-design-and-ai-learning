def int_reverse(data):
	if type(data) is not int:
		return None
	s = str(data)
	t = 1
	if s[0] == '+' or s[0] == '-':
		if s[0] == '-':
			t = -1
		s = s[1:]
	s = s[::-1]
	return int(s)*t

print(int_reverse(-100))