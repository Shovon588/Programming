n=int(input())
a=list(map(int,input().split()))

sasha=[0]*(n+1)
dima=[0]*(n+1)

for i in range(2*n):
     temp=a[i]
     if sasha[temp]==0:
          sasha[temp]=i+1
     else:
          dima[temp]=i+1


sa_in=1;di_in=1;total=0
for i in range(1,n+1):
     total+=abs(sasha[i]-sa_in)
     total+=abs(dima[i]-di_in)
     sa_in=sasha[i]
     di_in=dima[i]


print(total)
