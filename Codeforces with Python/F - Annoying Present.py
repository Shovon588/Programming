n,m=map(int,input().split())
result=0
for i in range(m):
    x,d=map(int,input().split())
    result+=(n*x)+d*(n-1)*(n/2)

print(result/n)
