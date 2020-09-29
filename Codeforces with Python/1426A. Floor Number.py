from math import ceil
for I in range(int(input())):
    n,x = map(int,input().split())

    if n <= 2:
        print(1)
    else:
        n = n-2
        print(ceil(n/x)+1)
