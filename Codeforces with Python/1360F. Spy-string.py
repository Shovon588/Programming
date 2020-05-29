for I in range(int(input())):
    n,m = map(int,input().split())

    flag=[[] for i in range(n)]
    check2=''
    for i in range(n):
        s = input()
        if i==0:
            check=s
            
        if i>0:
            for j in range(m):
                if check[j]!=s[j]:
                    flag[i].append(j)
            if len(flag[i])==2:
                check2=s

    temp1='okay'; temp2=[]
    for i in range(n):
        if len(flag[i])>2:
            temp1='problem'
        if len(flag[i])==2 and len(temp2)==0:
            temp2=flag[i]

    first=0; second=0
    for i in range(n):
        if temp2[0] in flag[i]:
            first+=1
        elif temp2[1] in flag[i]:
            second+=1
        else:
            temp1='problem'

    if temp1=='problem':
        print(-1)
    else:
        if len(temp2)==2:
            check=list(check)
            if first>second:
                to_change=temp2[0]
            else:
                to_change=temp2[1]
            check[to_change] = check2[to_change]
            print(''.join(check))
        else:
            print(check)
    if I==25:
        break

"""
10 10
zjqtlkifyd
zjctlkiqyd
zjqtlkiqyd
zjqtlkixyd
zjqtikiqyd
zjqtlkiqid
zjqolkiqyd
zjqtlkiqrd
zjqtlxiqyd
njqtlkiqyd
"""
#zjqtlkiqyd
