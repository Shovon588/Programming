n = int(input())
a = list(map(int,input().split()))
k = int(input())

count=0
for i  in range(n-1):
    for j in range(i+1,n):
        if (a[i]+a[j])%k==0:
            count+=1
