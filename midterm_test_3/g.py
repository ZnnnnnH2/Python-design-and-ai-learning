def total_ascend(h):
	length = len(h)
	ans = 0
	cons = [0]
	for i in range(1,length):
		if h[i] > h[i - 1]:
			cons.append(cons[i-1] + 1)
		else:
			if cons[i-1] > 0:
				ans+=1
			cons.append(0)
	if cons[-1] > 0:
		ans+=1
	return ans

print(total_ascend([100, 80, 150, 250]))