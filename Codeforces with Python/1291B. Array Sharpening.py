for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))

    flag='first';jinis=0;count=0
    
    for i in a:
        if flag=='first':
            print(i,jinis,flag)
            if i>=jinis:
                jinis+=1
            else:
                print('ekhane')
                jinis=min(jinis-3,i-1)
                flag='second'
                
            count+=1
        else:
            if i>=jinis and jinis>=0:
                jinis-=1
                count+=1
            elif i<jinis:
                jinis=i-1
                count+=1
            else:
                flag='holo na'
                break
                   
    if count==n:
        print('YES')
    else:
        print('NO')
