n,m = map(int,input().split())
a = list(map(int,input().split()))

sum=0;flag=0;
for i in range(n):
    sum+=a[i]

    temp=sum//m
    print(temp-flag,end=' ')
    flag=temp
