j=1
while(True):
    try:
        n,m=map(int,input().split())
        b=list(map(int,input().split()))
        b=str(b)
        flag=-1
        
        for i in range(1,11):
            n=n*i
            a=str(n)
            a=list(a)
            
            c=set(a) & set(b)

            if len(c)==0:
                print('Case ',j,': ',n)
                flag=1
                break

        if flag==-1:
            print('Case ',j,': -1',)
        j=j+1
        
    except EOFError:
        break
