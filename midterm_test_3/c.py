def simplified_zigzag(l):
	m = len(l)
	n = len(l[0])
	for i in l:
		if len(i) != n:
			return []
	i, j = 0, 0
	ans = []
	while i + j < m + n - 1:
		if i < m and j < n:
			ans.append(l[i][j])
		i += 1
		j -= 1
		if j < 0:
			j, i = i, 0
	return ans


print(simplified_zigzag([[1, 2, 3, 4],
						 [5, 6, 7, 8],
						 [9, 10, 11, 12]]))
print(simplified_zigzag([['A', 'B', 'C'],
						 ['D', 'E', 'F'],
						 ['G', 'H', 'I'],
						 ['J', 'K', 'L'],
						 ['M', 'N', 'O']]))
