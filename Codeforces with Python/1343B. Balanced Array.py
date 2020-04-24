t = int(input())

for i in range(t):
    n = int(input())

    if (n//2)%2==1:
        print('NO')
    else:
        print('YES')
        even=0; prt=2
        for j in range((n//2)):
            print(prt,end=' ')
            even+=prt
            prt+=2


        odd=0;prt=1
        for j in range((n//2)-1):
            print(prt,end=' ')
            odd+=prt
            prt+=2

        print(even-odd)
            
            
        
