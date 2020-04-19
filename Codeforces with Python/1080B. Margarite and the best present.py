for i in range(int(input())):
    a,b=map(int,input().split())
    temp=(b-a+1)
    if temp%2!=0:
        total=((a+b)*(temp//2))+(a+b)//2
    else:
        total=(a+b)*(temp//2)

    if a%2!=0 and b%2!=0:
        n=temp-((b-a)//2)
    elif a%2==0 and b%2==0:
        n=(b-a)//2
        a+=1;b-=1
    else:
        n=temp//2
        if a%2==0:
            a+=1
        else:
            b-=1

    neg=int((n/2)*(a+b))
    pos=total-neg
    print(pos,neg)
    print(pos-neg)
