n,m=map(int,input().split())
result=0
for i in range(m):
    a,b,c=map(int,input().split())
    result=result+((b-a)+1)*c
print(result//n)
