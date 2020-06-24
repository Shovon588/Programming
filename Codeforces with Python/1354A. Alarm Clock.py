from math import ceil

for _ in range(int(input())):
    a,b,c,d = map(int,input().split())
    if b>=a:
        print(b)
    else:
        rem = a-b

        if c-d<1:
            print(-1)
        else:
            print(c*ceil((rem/(c-d)))+b)
