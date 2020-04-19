n = int (input())


for i in range (n):
    a = input()
    b = len(a)

    if (a[b-2]=='c' and a[b-1]=='h') or a[b-1]=='x' or a[b-1]=='s' or a[b-1]=='o':
        print (a+'es')
    elif (a[b-2]=='f' and a[b-1]=='e') or a[b-1]=='f':
        if a[b-2]=='f' and a[b-1]=='e':
            print (a[:-2]+'ves')
        else:
            print (a[:-1]+'ves')
    elif a[b-1]=='y':
        print (a[:-1]+'ies')
    else:
        print (a+'s')
        
