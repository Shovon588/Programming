from math import sqrt

for I in range(int(input())):
    n = int(input())
    if n==0:
        print(0)
    else:
        if sqrt(n)==int(sqrt(n)):
            n = int(sqrt(n))
            n = n-2
            result = (n*(n+1))//2
            print(result)
        else:
            print(0)

    
