for _ in range(int(input())):
    n,k=map(int,input().split())
    s=input()

    zero = s.count('0')
    one = s.count('1')
    dif = zero-one

    flag = 0;res = 0
    if dif==0:
        flag='infinite'
    elif dif<0:
        flag=0
    elif k==0:
        flag='empty'
    else:
        flag = (n/dif)*k
        if flag==int(flag):
            res+=1
        else:
            flag=0
    
    if flag=='infinite':
        print(-1)
    elif  flag=='empty':
        print(1)
    elif flag==0:
        print(0)
    else:
        temp = s[::-1]
        z=0;o=0;count=0
        for i in temp:
            if i=='0':z+=1
            if i=='1':o+=1
            if z>0 and o>0 and z==o:
                count+=1
        res+=count
        temp = s
        z=0;o=0;count=0
        for i in temp:
            if i=='0':z+=1
            if i=='1':o+=1
            if z>0 and o>0 and z==o:
                count+=1
        res+=count

        print(res)
            
        
