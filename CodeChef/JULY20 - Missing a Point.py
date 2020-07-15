for I in range(int(input())):
    n = int(input())

    startsat = {}
    endsat = {}
    for i in range((4*n)-1):
        a,b = map(int,input().split())

        if a in startsat:
            startsat[a] += 1
        else:
            startsat[a] = 1

        if b in endsat:
            endsat[b] += 1
        else:
            endsat[b]= 1

    start = -1
    end = -1
    for key in startsat:
        if startsat[key]%2==1:
            start=key
            break

    for key in endsat:
        if endsat[key]%2==1:
            end=key
            break

    print(start,end)
        
