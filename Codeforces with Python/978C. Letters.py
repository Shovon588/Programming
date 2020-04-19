n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

for i in range(1,n):
     a[i]+=a[i-1]

flag=0;j=0;check=a[j]

for i in range(m):
     if b[i]<=check:
          print(j+1,b[i]-flag)
     else:
          flag=a[j]
          j+=1;check=a[j]
          print(j+1,b[i]-flag)
