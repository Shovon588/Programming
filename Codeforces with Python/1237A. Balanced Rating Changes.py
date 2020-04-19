from math import ceil,floor
n=int(input())

cal=1
for i in range(n):
    a=int(input())
    if a%2==0:
        print(a//2)
    else:
        if cal%2==1:
            print(floor(a/2))
            cal+=1
        else:
            print(ceil(a/2))
            cal+=1
