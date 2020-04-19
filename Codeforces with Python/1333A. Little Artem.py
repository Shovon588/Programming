for z in range(int(input())):
    n,m = map(int,input().split())

    str1 = ('BW'*m)[:m]
    str2 = ('WB'*m)[:m]

    print('WW',end='')
    print(str1[:m-2])
    for i in range(n-1):
        if i%2==0:
            print(str1)
        else:
            print(str2)
