while(True):
    try:
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        c=set(a) & set(b)
        c=list(c)
        c.sort()
        total=0

        inia=1
        inib=1
        for i in range(len(c)):
            ina=a.index(c[i])
            inb=b.index(c[i])
            suma=sum(a[inia:ina])
            sumb=sum(b[inib:inb])

            inia,inib=ina,inb
            if suma>=sumb:
                total+=suma
            else:
                total+=sumb

        suma=sum(a[inia:])
        sumb=sum(b[inib:])
        

        if suma>=sumb:
            total+=suma
        else:
            total+=sumb

        
        print(total)

        
        

    except EOFError:
        break
