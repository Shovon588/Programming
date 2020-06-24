for I in range(int(input())):
    n,x = map(int,input().split())
    a = list(map(int,input().split()))

    
    odd = 0
    even = 0

    for num in a:
        if num%2==0:even+=1
        else:odd+=1

    if even==0:
        if x%2==1:
            print('Yes')
        else:
            print('No')
    elif even<x:
        x-=even
        if odd>=x:
            if x%2==1:
                print('Yes')
            else:
                if odd>=x+1:
                    print('Yes')
                else:
                    print('No')
        else:
            print('No')
    else:
        if odd>0:
            print('Yes')
        else:
            print('No')

        
            
