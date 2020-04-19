n=int(input())
a=list(map(int,input().split()))

count=1;temp=a[0]

for i in range(1,n):
     if i+1>temp:
          count+=1
          temp=a[i]
     else:
          if a[i]>temp:
               temp=a[i]
print(count)
