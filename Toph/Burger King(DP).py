def king(i,bud,k):
    if i>=n or k==K:
        if bud==0 and k==K:return 1
        else:return 0
        
    try:
        if dic[i][bud]:
            print('hmmm')
            return dic[i][bud]
    except KeyError:
        pass

    ret1=0;ret2=0

    if bud-price[i]>=0:
        ret1=king(i+1,bud-price[i],k+1)

    ret2=king(i+1,bud,k)
    temp=ret1+ret2
    dic1={}
    dic1[bud]=temp
    dic[i]=dic1
    return dic[i][bud]
    

for i in range(int(input())):
    n=int(input())
    K=int(input())
    bud=int(input())
    price=list(map(int,input().split()))
    dic={}

    print("Case %d: %d"%(i+1,king(0,bud,0)))

    
