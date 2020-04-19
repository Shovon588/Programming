n,m=map(int,input().split())

low=min(n,m)
high=max(n,m)

for i in range(low+1,high+2):
    print(i)
