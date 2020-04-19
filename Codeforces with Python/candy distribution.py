n,m = map(int,input().split())

a = list(map(int,input().split()))

count=0
for i in range(n):
    flag=a[i]
    if a[i]%m==0:
        count+=1

    for j in range(i+1,n):
        flag+=a[j]
        if flag%m==0:
            
            count+=1


print(count)
