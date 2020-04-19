n=int(input())

a=list(map(int,input().split()))

a.sort()

count=0
for i in range(n-1):
    for j in range(i+1,n):
        if a[i]>0 and a[j]%a[i]==0:
            a[j]=-1

a.sort(reverse=True)

count=0
for i in a:
    if i<0:break
    else:count+=1

print(count)
