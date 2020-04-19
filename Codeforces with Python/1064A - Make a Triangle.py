a=list(map(int,input().split()))
b=max(a);c=sum(a)-b

if c>b:print(0)
else:print((b+1)-c)
