n=int(input())
a=list(map(int,input().split()))
total=0
for i in range(n):
    if a[i]==1:
        total+=1
    elif a[i]%2!=0:
        total+=a[i]+1
    else:
        while a[i]%2==0:
            total+=a[i]
            a[i]=a[i]//2

        if a[i]==1:
            total+=1
        elif a[i]>1:
            total+=a[i]+1

print(total)
