for I in range(int(input())):
    a,b,n = map(int,input().split())
    res=0
    while(1):
        res+=1
        a, b = min(a,b)+max(a,b),max(a,b)
        if a>n:
            break

    
    print(res)
