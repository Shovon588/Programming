for I in range(int(input())):
    n,m,x,y = map(int,input().split())

    result=0
    for i in range(n):
        s = input()

        if 2*x<=y:
            for i in range(m):
                if s[i]=='.':
                    result+=x

        else:
            flag=''
            i=0
            while(i<m-1):
                if s[i]=='.' and s[i+1]=='.':
                    result+=y
                    if i+1==m-1:
                        flag='done'
                    i+=1
                elif s[i]=='.':
                    result+=x
                    if i==m-1:
                        flag='done'
                i+=1
                
            if len(s)>1:
                if flag=='':
                    if s[-1]=='.':
                        result+=x
            else:
                if s[0]=='.':
                    result+=x

    print(result)
