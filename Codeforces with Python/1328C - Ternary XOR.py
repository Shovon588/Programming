for _ in range(int(input())):
    n = int(input())
    string = input()

    s='';t='';flag=''
    for i in range(n):
        if flag=='':
            if string[i]=='2':
                s+='1'
                t+='1'
            elif string[i]=='0':
                s+='0'
                t+='0'
            else:
                if flag=='':
                    s+='1'
                    t+='0'
                    flag='done'
        else:
            s+='0'
            t+=string[i]
    print(s)
    print(t)
            
