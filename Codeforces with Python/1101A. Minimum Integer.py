from math import ceil

for i in range(int(input())):
    l,r,d=map(int,input().split())
    temp=d
    if temp<l:
        print(temp)
    else:
        temp=ceil(r/d)
        if temp*d==r:
            print(d*(temp+1))
        else:
            print(temp*d)
