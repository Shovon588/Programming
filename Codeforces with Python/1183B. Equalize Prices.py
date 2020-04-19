for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    mina=min(a);maxa=max(a)

    if maxa-k<=mina+k:
        print(mina+k)
    else:
        print(-1)
