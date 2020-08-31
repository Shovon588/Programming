from math import ceil

n = int(input())
a = list(map(int,input().split()))

print(1,1)
print(a[0]*(n-1))

if n>=2:
    print(2,n)
    for i in range(1,n):
        print((n-1)*a[i],end=' ')
else:
    print(1,1)
    print(0)

print(1,n)
for i in range(n):
    print((((n-1)*a[i])+a[i])*-1,end=' ')
        
