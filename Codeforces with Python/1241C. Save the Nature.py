for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    x1,y1=map(int,input().split())
    x2,y2=map(int,input().split())

    target=int(input())

    if x1>=x2:
        fx=x1;fy=y1;sx=x2;sy=y2
    else:
        fx=x2;fy=y2;sx=x1;sy=y1
