n=int(input())
a=list(map(int,input().split()))

sum=0
for i in range(n):
    sum+=(i*a[i]*2)

print(sum*2)
