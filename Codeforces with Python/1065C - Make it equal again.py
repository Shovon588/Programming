n,k=map(int,input().split())
a=list(map(int,input().split()))
b=[0]*300000
mx=max(a)
mn=min(a)
for i in a:
    b[i]+=1

c=0;t=b[mx];s=t

while mx>(mn+1):
    while s+t+b[mx-1]<=k:
        mx-=1
        t+=b[mx]
        s+=t
        
    s=0
    c+=1

print(c)
