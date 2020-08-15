n = int(input())
a = list(map(int,input().split()))

count=0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if a[i]+a[j]>a[k] and a[j]+a[k]>a[i] and a[i]+a[k]>a[j]:
                if a[i]!=a[j] and a[i]!=a[k] and a[j]!=a[k]:
                    count+=1

print(count)
    
