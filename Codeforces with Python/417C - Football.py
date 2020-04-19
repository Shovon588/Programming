n,k=map(int,input().split())

if 2*k>=n:print(-1)
else:
	print(n*k)
	for i in range(n):
		for j in range(k):
			print (i+1,(i+j+1)%n+1)
