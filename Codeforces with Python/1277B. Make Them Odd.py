for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))

    dic={};l=[]

    for num in a:
        try:
            if dic[num]:
                pass
        except KeyError:
            dic[num]=1
            l.append(num)
    l.sort(reverse=True)

        
