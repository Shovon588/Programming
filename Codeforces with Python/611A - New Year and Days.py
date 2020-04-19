a,b,c = input().split()
a = int (a)

if c[0]=='m':
    if a>=1 and a<=29:
        print ('12')
    elif a==30:
        print ('11')
    elif a==31:
        print ('7')
        
else:
    if a==5 or a==6:
        print ('53')
    else:
        print ('52')
