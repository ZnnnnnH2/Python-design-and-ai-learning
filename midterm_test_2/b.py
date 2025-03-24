def password_check(a):
	if type(a) is not str:
		return False
	length = len(a)
	if not 6<=length<=12:
		return False
	flag1 = False
	flag2 = False
	flag3 = False
	for i in a:
		if 'a' <=i<='z':
			flag1 = True
		elif 'A' <=i<='Z':
			flag2 = True
		elif '0' <=i<='9':
			flag3 = True

	if not (flag1 and flag2 and flag3):
		return False

	flag1 = False
	flag2 = False
	flag3 = False

	if '$' in a:
		flag1 = True
	if '@' in a:
		flag2 = True
	if '#' in a:
		flag3 = True
	if not (flag1 or flag2 or flag3):
		return False

	return True

print(password_check("a1b2c3d4e5"),password_check("a1b2c3d4E@"),password_check(123))