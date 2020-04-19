n=int(input())
check=[]
for i in range(n):
     a,b=map(int,input().split())
     check.append(b)

k=int(input())

for i in check:
     if k>i:
          n-=1

print(n)
