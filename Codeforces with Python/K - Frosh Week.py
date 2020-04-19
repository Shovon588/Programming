n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a.sort()
b.sort()
count=0
for i in a:
    for j in range(m):
        if b[j]>=i:
            b[j]=b[j]-i
            count+=1
            break
print(count)
