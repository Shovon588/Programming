def result(n):
     n-=1;return ((n*(n+1))//2)

n,m=map(int,input().split())

max=result(n-(m-1))

temp1=n//m
temp2=n%m

min=(result(temp1+1))*temp2
min+=(result(temp1))*(m-temp2)

print(min,max)
