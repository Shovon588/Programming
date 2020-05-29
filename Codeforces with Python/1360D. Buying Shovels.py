from math import sqrt, ceil
for I in range(int(input())):
    n,k = map(int,input().split())

    res=[n]
    for i in range(1,ceil(sqrt(n)+1)):
        if n%i==0:
            if k>=(n//i):
                res.append(i)
            temp = n//i
            if k>=(n//temp):
                res.append(temp)
            
    print(min(res))
