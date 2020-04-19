n=int(input())
a=list(map(int,input().split()))

a.sort()

count=0
for i in range(0,n-1,2):
    if a[i]!=a[i+1]:
        count+=a[i+1]-a[i]

print(count)
