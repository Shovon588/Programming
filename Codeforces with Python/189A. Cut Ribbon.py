n,a,b,c = map(int,input().split())

mini = min(min(a,b),c)
res = n//mini
rem = n%mini
