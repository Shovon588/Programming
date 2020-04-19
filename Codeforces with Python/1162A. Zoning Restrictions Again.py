n,h,m=map(int,input().split())

li=[h]*(n+1)

for _ in range(m):
     l,r,x=map(int,input().split())
     for i in range(l,r+1):
          li[i]=min(li[i],x)
          
res=0
for i in range(1,n+1):
     res+=(li[i]*li[i])
