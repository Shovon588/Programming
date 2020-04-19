n=int(input())
a=list(map(int,input().split()))
a.sort()
print(a)
sum1=sum(a)

for i in range(n):
    a[i]=a[i]*-1
print(a)
sum2=sum(a)

if sum1>=sum2:
    print(sum1)
else:
    print(sum2)
