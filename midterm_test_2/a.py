def sort_odd_and_even(a):
	if type(a) is not list:
		return None
	even = []
	odd = []
	length = len(a)
	for i in range(length):
		if type(a[i]) is not int:
			return None
		if a[i] % 2 == 1:
			odd.append(a[i])
		else:
			even.append(a[i])
	odd.sort(reverse=True)
	even.sort()
	return odd+even

print(sort_odd_and_even([1.3, 2, 3]))
print(sort_odd_and_even([1, 2, 3, 4, 5]))
print(sort_odd_and_even([1, 3, 5, 7]))
print(sort_odd_and_even([]))