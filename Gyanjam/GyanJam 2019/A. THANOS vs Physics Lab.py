avoid='+-*/'

for x in range(int(input())):
    s=input()

    div=s.count('/')
    mul=s.count('*')

    for j in range(div):
        l=len(s)
        pos=s.index('/')
        left=''
        right=''

        for j in range(pos+1,l):
            if s[j] not in avoid:
                right+=s[j]
                r=j
            else:
                break

        for j in range(pos-1,-1,-1):
            if s[j] not in avoid:
                left+=s[j]
                l=j
            else:
                break
        left=left[::-1]
        temp=str(int(left)//int(right))
        if l==0:
            s=s[:l]+temp+s[r+1:]
        else:
            s=s[:l]+temp+s[r+1:]



    for j in range(mul):
        l=len(s)

        pos=s.index('*')
        left=''
        right=''

        for j in range(pos+1,l):
            if s[j] not in avoid:
                right+=s[j]
                r=j
            else:
                break

        for j in range(pos-1,-1,-1):
            if s[j] not in avoid:
                left+=s[j]
                l=j
            else:
                break
        left=left[::-1]

            
        temp=str(int(left)*int(right))
        s=s[:l]+temp+s[r+1:]


    if s[0]!='-':
        s='+'+s
    
    l=len(s)
    total=0;

    for i in range(l):
        num=''
        if s[i]=='+':
            
            for j in range(i+1,l):
                if s[j] not in avoid:

                    num+=s[j]
                else:
                    i=j
                    break
            total+=int(num)
        elif s[i]=='-':
            for j in range(i+1,l):
                if s[j] not in avoid:
                    num+=s[j]
                else:
                    i=j
                    break
            total-=int(num)
                
    
    print('Case %d: %d'%(x+1,total))






