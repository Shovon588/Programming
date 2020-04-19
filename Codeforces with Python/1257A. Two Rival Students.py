for _ in range(int(input())):
    n,x,a,b=map(int,input().split())
    l,h=min(a,b),max(a,b)

    if l-1<=x:
        x=x-(l-1);l=1
    else:
        l=l-x
        x=0
    if n-h<=x:
        h=n
    else:
        h=h+x

    print(h-l)
