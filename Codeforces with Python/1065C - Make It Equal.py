n,k=map(int,input().split())
a=list(map(int,input().split()))

b=[]
for i in a:
    if i not in b:
        b.append(i)
b.sort()
b=b[::-1]
c=len(b);count=0;cnt=0;result=0
for i in range(c-1):
    d=a.count(b[i])
    count+=d
    z=count*(b[i]-b[i+1])
    if cnt+z>k and z<=k:
        result+=1
        cnt=z
    else:
        cnt+=z
if cnt>0 and cnt<=k:
    result+=1
print(result)
