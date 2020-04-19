while True:
    a=list(map(int,input().split()))
    if a[0]==0:
        break
    b=list(map(int,input().split()))

    c=[];d=[];count=0

    temp=1
    for i in range(a[0]):
        for j in range(temp,b[0]):
            if a[i]==b[j]:
                c.append(i)
                d.append(j)
                temp=j
    
    tempc=1;tempd=1
    for i in range(len(c)):
        temp1=sum(a[tempc:c[i]])
        tempc=c[i]
        temp2=sum(b[tempd:d[i]])
        tempd=d[i]
        count+=max(temp1,temp2)

    count+=max(sum(a[tempc:]),sum(b[tempd:]))

    print(count)
