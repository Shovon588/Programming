for _ in range(int(input())):
    n,m=map(int,input().split())

    total=n//m

    a=[]

    for i in range(1,10):
        a.append((i*m)%10)

    temp=total//10

    result=sum(a)*temp
    temp=total%10

    result+=sum(a[:temp])

    print(result)
