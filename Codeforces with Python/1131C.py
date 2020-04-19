n=int(input())

a=list(map(int,input().split()))
result=[0]*(n+1)

a.sort()

j=1
for i in range(0,n,2):
     try:
          result[j]=a[i]
          result[-j]=a[i+1]
          j+=1
     except IndexError:
          break
a=result[1:]

print(*a)
