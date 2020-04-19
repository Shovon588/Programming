for _ in range(int(input())):
    s,t=map(str,input().split())
        
    temp1=[];temp2=[];res=[]
    ls=len(s);lt=len(t)
    
    for i in range(ls):
        temp1.append((s[i],i))
        temp2.append((s[i],i))
        res.append(s[i])
        
    temp2.sort()
    
    flag1=[0,10000]
    flag2=[0,10000]
    for i in range(ls):
        if temp2[i][0]<temp1[i][0] and temp2[i][1]>temp1[i][1]:
            flag1=list(temp1[i]);flag2=list(temp2[i])
            break

    pres=[]
    for i in range(ls):
        if i==flag1[1]:
            pres.append(flag2[0])
        elif i==flag2[1]:
            pres.append(flag1[0])
        else:
            pres.append(res[i])

    flag=''
    for i in range(min(ls,lt)):
        if pres[i]!=t[i]:
            if pres[i]<t[i]:
                print(''.join(pres))
                flag='done'
                break
            else:
                print('---')
                flag='done'
                break
            
    if flag=='':
        if ls<lt:
            print(''.join(pres))
        else:
            print('---')
