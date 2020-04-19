from math import ceil
for _ in range(int(input())):
    n,g,b = map(int,input().split())

    half = ceil(n/2)

    good_needed = ceil(half/g)
   

    total=0
    total = (good_needed-1)*g
    total+= half-total
    total+= (good_needed-1)*b

    if total<n:
        print(n)
    else:
        print(total)

