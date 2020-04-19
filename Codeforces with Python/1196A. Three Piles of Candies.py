for i in range(int(input())):
    a=list(map(int,input().split()))
    maxa=max(a)
    mina=min(a)
    mida=sum(a)-maxa-mina

    alice=mida
    bob=mina

    temp=alice-bob

    bob+=temp

    maxa-=temp

    alice+=(maxa//2)

    print(alice)
