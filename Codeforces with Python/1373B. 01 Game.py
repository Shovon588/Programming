for I in range(int(input())):
    s = input()
    l = len(s)
    ll = len(s)
    while(1):
        s = s.replace('01','')
        s = s.replace('10','')

        if len(s)==ll:
            break
        else:
            ll = len(s)
    
    diff = (l-ll)//2

    if diff%2==1:
        print("DA")
    else:
        print("NET")
