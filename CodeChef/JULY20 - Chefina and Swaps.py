for I in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    a.sort()
    b.sort()
    
    dic = {}
    dica = {}
    dicb = {}

    for num in a:
        if num in dic:
            dic[num]+=1
        else:
            dic[num]=1

        if num in dica:
            dica[num]+=1
        else:
            dica[num]=1

    for num in b:
        if num in dic:
            dic[num]+=1
        else:
            dic[num]=1

        if num in dicb:
            dicb[num]+=1
        else:
            dicb[num]=1

    flag=True
    for key in dic:
        if dic[key]%2!=0:
            flag=False
            break

    if flag:
        changeable_a = []
        changeable_b = []
        length = 0
        mini = 1000000000

        for num in dica:
            mini = min(mini,num)
            numinall = dic[num]
            numina = dica[num]
            diff = numina - numinall//2
            if diff>0:
                for i in range(diff):
                    changeable_a.append(num)
                    length+=1
        
        for num in dicb:
            mini=min(mini,num)
            numinall = dic[num]
            numinb = dicb[num]
            diff = numinb - numinall//2
            if diff>0:
                for i in range(diff):
                    changeable_b.append(num)
        

        changeable_a.sort()
        changeable_b.sort(reverse=True)

        res = 0
        for i in range(length):
            res+=min(2*mini,min(changeable_a[i],changeable_b[i]))
        print(res)
        
    else:
        print(-1)
