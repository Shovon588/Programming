t=int(input())
for i in range(t):
    
    n=int(input())
    total=0
    countc=0;top=0;side=0;tempt=0;temps=0;
    
    for j in range(n):
        c,k=input().split()
        a=int(k)
        
        if c=='C':
            countc+=1
            if countc==2:
                tempt=a
            if countc==3:
                temps=a

        if countc==1:
            top=a+top
        elif countc==2:
            side=side+a

    
        if c=='C':
            total=total+(a*a)
        elif c=='S':
            total=total+(a*a)
        elif c=='T':
            total=total+(0.4330127018922193*a*a)

    top=top+tempt
    side=side+temps
    result=(top*side)-total
    print("%.4f" %result)
            
