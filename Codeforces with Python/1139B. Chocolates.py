n=int(input())
a=list(map(int,input().split()))
a=a[::-1]

res=a[0];temp=a[0]

for i in range(1,n):
     if a[i]<temp:
          res+=a[i]
          temp=a[i]
     else:
          if temp-1>0:
               res+=(temp-1)
               temp=temp-1
print(res)
