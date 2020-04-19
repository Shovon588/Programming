for _ in range(int(input())):
    n,m,q=map(int,input().split())

    who=[];whom=[]
    for i in range(m):
        a,b=map(int,input().split())
        who.append(a)
        whom.append(b)

    free=[]
    for i in range(q):
        a=int(input())
        free.append(a)

    j=q+1;count=0
    for i in range(j):
        try:
            if free[i] in who:
                temp=who.index(free[i])
                if whom[temp] not in free:
                    count+=1
                    free.append(whom[temp])
                    j+=1
        except IndexError:
            break

    print(q+count)


