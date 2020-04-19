from math import ceil
for _ in range(int(input())):
    a,b = map(int,input().split())

    if a%b==0:
        print(0)
    else:
        temp= a/b
        c = ceil(temp)
        print(abs((c*b)-a))
