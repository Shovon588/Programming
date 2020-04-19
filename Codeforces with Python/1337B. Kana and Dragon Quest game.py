from math import ceil

for _ in range(int(input())):
    h,n,m = map(int,input().split())

    while(h>20 and n>0):
        h = (h//2)+10
        n-=1
    if ceil(h/10)<=m:
        print('YES')
    else:
        print('NO')
