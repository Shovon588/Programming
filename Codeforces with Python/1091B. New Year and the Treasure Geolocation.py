n=int(input())

x=0;y=0
for i in range(2*n):
    a,b=map(int,input().split())
    x+=a;y+=b


print(x//n,y//n)
