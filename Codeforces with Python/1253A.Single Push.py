for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))

    dif=[];temp=0
    for i in range(n):
        if a[i]-b[i]!=0:
            dif.append(i)
            temp=b[i]-a[i]

    flag='YES'
    if len(dif)>1:
        for i in range(len(dif)-1):
            l=dif[i]
            if a[l]+temp==b[l] and temp>0 and dif[i]+1==dif[i+1]:
                pass
            else:
                flag='NO'
        print(flag)
    elif len(dif)==1:
        l=dif[0]
        if a[l]+temp==b[l] and temp>=0:
            print('YES')
        else:
            print('NO')
    else:
        print('YES')
