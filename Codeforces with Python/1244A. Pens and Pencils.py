from math import ceil

for _ in range(int(input())):
    a,b,c,d,k=map(int,input().split())

    temp1=ceil(a/c)
    temp2=ceil(b/d)

    if temp1+temp2>k:
        print(-1)
    else:
        print(temp1,temp2)
