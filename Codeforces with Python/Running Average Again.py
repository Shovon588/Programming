n=int(input())
a=list(map(int,input().split()))

res=0
for i in range(n):
    res+=a[i]
    temp=res/(i+1)

    if temp==int(temp):
        print(int(temp))
    else:
        print(temp)
