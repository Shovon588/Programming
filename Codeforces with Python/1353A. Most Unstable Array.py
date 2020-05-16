from math import ceil

for _ in range(int(input())):
    n,m = map(int,input().split())

    if n==1:
        print(0)
    else:
        print(min(2,n-1)*m)
