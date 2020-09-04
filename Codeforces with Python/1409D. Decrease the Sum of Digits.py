for I in range(int(input())):
    n,s = map(int,input().split())

    strn = str(n)

    totsum = 0
    for char in strn:
        totsum+=int(char)
        
    summ = 0
    i = -1
    while i<len(strn)-1 and summ+int(strn[i+1])<s:
        summ+=int(strn[i+1])
        i += 1

    if summ+1>s:
        i-=1

    if i==-1:
        if totsum<=s:
            final = strn
        else:
            final = '1'
            final += '0'*len(strn)
    else:
        print("i am here")
        final = strn[:i]
        final += str(int(strn[i])+1)
        final += ('0'*(len(strn)-i-1))
        

    print(int(final)-n)
    



        


    
