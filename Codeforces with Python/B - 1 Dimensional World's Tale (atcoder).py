n,m,x,y=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
amax=max(a)
bmin=min(b)
c=a+b;flag=0
for i in range(n+m):
    if (c[i]>x and c[i]<=y) and (amax<c[i]) and (bmin>=c[i]):
        print('No War')
        flag=1
        break
if flag==0:
    print('War')
