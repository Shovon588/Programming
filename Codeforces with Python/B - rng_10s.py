
for i in range(int(input())):
    temp=[]
    a,b,c,d = map(int,input().split())

    while(1):
        if a>=b:
            a=a-b
            if a in temp:
                flag=1
                break
            else:
                temp.append(a)

            if a<=c:
                a+=d
        else:
            flag=0
            break
        print(a)

    if flag==0:
        print('No')
    elif flag==1:
        print('Yes')
