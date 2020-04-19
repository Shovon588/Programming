for _ in range(int(input())):
    res=0
    a,b,c=map(int,input().split())

    if c//2<=b:
        res+=((c//2)+(2*(c//2)))
        b-=c//2;c-=(2*(c//2))
    else:
        res+=(b+(2*b))
        b=0
    if b//2<=a:
        res+=((b//2)+(2*(b//2)))
    else:
        res+=(a+(2*a))
    print(res)
        
