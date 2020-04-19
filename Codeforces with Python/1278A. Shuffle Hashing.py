for _ in range(int(input())):
    s=input()
    t=input()
    ls=len(s)
    lt=len(t)
    s=list(s)
    s.sort()
    flag=''
    for i in range(lt-ls+1):
        temp=list(t[i:i+ls])
        temp.sort()
        if temp==s:
            flag='hoisekaj'
            break

    if flag=='':
        print('NO')
    else:
        print('YES')
        
