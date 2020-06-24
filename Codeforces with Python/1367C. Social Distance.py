for I in range(int(input())):
    n,k = map(int,input().split())
    s = input()
    

    occupy = []
    for i,char in enumerate(s):
        if char=='1':
            occupy.append(i)

    result = 0
    
    if len(occupy)==0:
        for i in range(0,n,k+1):
            result+=1
    else:
        if occupy[0]!=0:
            left=0
            right=occupy[0]-k
            for i in range(left,right,k+1):
                result+=1

        for i in range(len(occupy)-1):
            left=occupy[i]+k
            right=occupy[i+1]-k
            for i in range(left+1,right,k+1):
                result+=1

        if occupy[-1]!=n-1:
            left=occupy[-1]+k
            right=n-1
            for i in range(left,right,k+1):
                result+=1

    print(result)
