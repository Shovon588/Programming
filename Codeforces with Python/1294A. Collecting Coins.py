for i in range(int(input())):
    a=list(map(int,input().split()))
    b = a.pop()

    boro = max(a)
    choto = min(a)
    majhari = sum(a)-boro-choto

    temp = boro-choto
    temp+= boro-majhari

    b = b-temp

    if b>=0 and b%3==0:
        print('YES')
    else:
        print('NO')
