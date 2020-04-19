for i in range(int(input())):
    s=input()
    s=s[-1]+s[-2]

    if s=='op':
        print('FILIPINO')
    elif s=='us':
        print('JAPANESE')
    elif s=='ad':
        print('KOREAN')
