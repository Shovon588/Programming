n,m=map(int,input().split())

res=100000
for i in range(n):
     a,b=map(int,input().split())
     temp=(a/b)*m
     res=min(res,temp)
print(res)
