n=int(input())
a=list(map(int,input().split()))

a.sort()

j=n-1;result=0
for i in range(n//2):
    result+=pow((a[i]+a[j]),2)
    j-=1

print(result)
