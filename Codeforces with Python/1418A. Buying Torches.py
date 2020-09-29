from math import ceil
for I in range(int(input())):
    x,y,n = map(int,input().split())

    stick_needed = (n*y)+(n-1)

    step = x-1

    res = stick_needed//step

    if res*step>=stick_needed:
        print(res)
    else:
        print(res+1)


