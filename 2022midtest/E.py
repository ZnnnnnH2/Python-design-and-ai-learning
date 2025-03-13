def dedup_2(list_a):
	dic = {}
	ans = []
	for i in list_a:
		if i not in dic:
			dic[i] = 1
			ans.append(i)
		else:
			dic[i] += 1
			if dic[i] <= 2:
				ans.append(i)
	return ans

print(dedup_2([1, 2, 3, 2, 3, 2, 1, 3, 5]))

print(dedup_2([1, 1, 1, 2, 3, 2, 1, 2,3]))