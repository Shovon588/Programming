for I in range(int(input())):
    n,m,k = map(int,input().split())

    temp = n//k

    if m<=temp:
        print(m)
    else:
        m-=temp
        k-=1
        if m%k==0:
            print(temp-(m//k))
        else:
            print(temp-((m//k)+1))
