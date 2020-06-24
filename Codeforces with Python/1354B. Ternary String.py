for _ in range(int(input())):
    s = input()

    flag=[]
    count = 0
    temp=''
    mini=100000005
    
    for char in s:
        if char not in flag:
            flag.append(char)

        if temp=='':
            count=1
            temp=char
        elif char==flag[0]:
            flag.remove(flag[0])
            flag.append(char)

            if len(flag)==2:
                count=2
        else:
            count+=1

        if len(flag)==3:
            mini=min(mini,count)

    if len(flag)==3:
        print(mini)
    else:
        print(0)
