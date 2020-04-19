n,h,a,b,k = map(int,input().split())


for i in range(k):
    temp=0
    ta,fa,tb,fb = map(int,input().split())

    if fa>=a and fa<=b:
        temp=abs(tb-ta)
        if fb>fa:
            temp+=abs(fb-fa)
        elif fa>fb:
            temp+=abs(fa-fb)

    if fa>b:
        temp+=abs(fa-b)
        fa=b
        temp+=abs(tb-ta)
        if fb>fa:
            temp+=abs(fb-fa)
        elif fa>fb:
            temp+=abs(fa-fb)

    if fa<a:
        temp+=abs(a-fa)
        fa=a
        temp+=abs(tb-ta)
        if fb>fa:
            temp+=abs(fb-fa)
        elif fa>fb:
            temp+=abs(fa-fb)

    print(temp)
