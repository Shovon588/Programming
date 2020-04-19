n,m=map(int,input().split())

a=list(map(int,input().split()))
a.sort()

temp=1;top=0;side=0;total=sum(a)


for i in range(n):
    if i==0:
        top+=1;side+=1;total-=1
    elif a[i]==temp:
        top+=1;total-=1
    elif a[i]>temp:
        side+=1;top+=1
        temp+=1;total-=1

if side<a[n-1]:
    total-=(a[n-1]-side)

if n==1:
    print(0)
else:
    print(total)
