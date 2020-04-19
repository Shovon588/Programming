n,k=map(int,input().split())
temp=n/2

if temp>=k:
     result=k-1+2+1+3+(n-2)*3
else:
     result=(n-k)+2+1+3+(n-2)*3
print(result)
