n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=a+b;d=[]
for i in c:
    if i not in d:
        d.append(i)
d.sort()
print(*d)
