def frog_climb_stairs(N):
	ans = [1,1]
	for i in range(2,N+1):
		ans.append(ans[i-1]+ans[i-2])
	return ans[N]

print(frog_climb_stairs(4))