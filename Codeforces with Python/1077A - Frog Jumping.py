t=int(input())
for i in range(t):
    a,b,k=map(int,input().split())
    if k%2==0:temp=k//2
    else:temp=k//2+1

    print((a*temp)-(b*(k-temp)))
