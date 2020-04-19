for i in range(int(input())):
    n,m=map(int,input().split())

    candy = (n//m)*m
    extra = n%m

    candy+=min(extra,m//2)

    print(candy)

    
