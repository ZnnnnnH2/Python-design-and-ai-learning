def hanio(n,a,b,c):
	if n==1:
		print(a,'-->',c)
		return
	hanio(n-1,a,c,b)
	print(a,'-->',c)
	hanio(n-1,b,a,c)
n = int(input())
hanio(n,'A','B','C')