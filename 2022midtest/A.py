def abstract_value(a):
	if type(a) == int:
		return abs(a)
	elif type(a) == float:
		return abs(a)
	elif type(a) == str:
		length = len(a)
		flag = True
		mun = -1
		for i in range(length):
			if '9' >= a[i] >= '0':
				continue
			elif a[i] == '.' and mun == -1:
				mun = i
			elif a[i] == '-' and i == 0:
				continue
			else:
				flag = False
				break
		if flag and mun != length -1:
				return abs(float(a))
	return None

print(abstract_value(10))
print(abstract_value("-1.5"))
print(abstract_value((3, 2)))
print(abstract_value("a"))
print(abstract_value(".9"))