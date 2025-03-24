def recursive_digit_sum(a):
	if a<=9:
		return a
	s = str(a)
	b = 0
	for i in s:
		b += int(i)
	return recursive_digit_sum(b)

print(recursive_digit_sum(32),recursive_digit_sum(678),recursive_digit_sum(88888888888888))
