for _ in range(int(input())):
    n,m,k=map(int,input().split())
    a=list(map(int,input().split()))
    next=0


    for i in range(n-1):
        left=a[i];right=a[i+1]

        temp=left-right

        if temp>=0:
            m+=temp
            next+=1
        else:
            temp=abs(temp)
            if temp<=k:
                next+=1
            else:
                temp1=temp-k
                if m>=temp1:
                    m-=temp1
                    next+=1
                else:
                    break

    if next==n-1:
        print('YES')
    else:
        print('NO')
