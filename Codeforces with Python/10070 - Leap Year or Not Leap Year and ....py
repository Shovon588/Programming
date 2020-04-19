def divider(s,m):
    temp=len(s)

    c=0
    for i in range(temp):
        c=(int(s[i])+(c*10))%m
    if c==0:return 0
    else:return 1



while(1):
    try:
        a=int(input())
        a=str(a)
        flag=0
        if ((divider(a,4)==0 and divider(a,100)==1) or divider(a,400)==0):
            print('This is leap year.')
            leap=1
            flag=1

        if divider(a,15)==0:
            print('This is huluculu festival year.')
            flag=1

        if leap==1 and divider(a,55)==0:
            print('This is bulukulu festival year.')

        if flag==0:
            print('This is an ordinary year.')
        print()
        
    except ValueError:
        break
