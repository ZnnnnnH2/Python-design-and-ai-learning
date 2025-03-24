def is_divisible(a):
	if type(a) is not int:
		return "None"
	a = abs(a)
	def helper(mun):
		ans = 0
		s = str(mun)
		for i in s:
			if '0'<=i<='9':
				ans += int(i)
		return ans

	if a%helper(a) == 0:
		return "Yes"
	else:
		return "No"

print(is_divisible(123),is_divisible("-1.0f"),is_divisible(-102),is_divisible(10))