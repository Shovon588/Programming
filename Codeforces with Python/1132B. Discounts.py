n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
a.sort()
total=sum(a)

for i in range(m):
     temp=b[i]
     print(total-(a[-temp]))
