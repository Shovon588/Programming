n=int(input())
a,b=map(int,input().split())

w1=1;w2=1
b1=n;b2=n

if a==w1 and b==w2:
    print('White')
elif a==b1 and b==b2:
    print('Black')
else:
    i=0
    while(1):
        i+=1
        if i%2!=0:
            if a==w1:
                w2+=1
            elif b==w2:
                w1+=1
            else:
                w1+=1;w2+=1
        else:
            if a==b1:
                b2-=1
            elif b==b2:
                b1-=1
            else:
                b2-=1;b1-=1

        if a==w1 and b==w2:
            print('White')
            break
            
        elif a==b1 and b==b2:
            print('Black')
            break
        
        
