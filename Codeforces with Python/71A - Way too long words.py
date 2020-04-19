for i in range (int(input())):
    a=input()
    
    b=int (len(a))

    if(b<=10):
        print (a)
    else:
        print (a[0]+str(b-2)+a[b-1])
