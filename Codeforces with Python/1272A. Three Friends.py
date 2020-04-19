for i in range(int(input())):
    a,b,c=map(int,input().split())

    first = min(a,b,c)
    third = max(a,b,c)
    second = (a+b+c)-(first+third)

    if first==second and second==third:
        pass
    elif first!=second and second!=third:
        first+=1;third-=1
    elif first==second and second!=third:
        if first+1==third:
            third-=1
        else:
            first+=1;second+=1;third-=1
    elif first!=second and second==third:
        if first+1==second:
            first+=1
        else:
            first+=1;second-=1;third-=1

    print(abs(first-second)+abs(second-third)+abs(first-third))

