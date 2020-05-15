for _ in range(int(input())):
    n = int(input())

    if n<4:
        print(-1)
    else:
        
        if n%2==0:
            for num in range(n-1,-1,-2):
                print(num,end=' ')
        else:
            for num in range(n,-1,-2):
                print(num,end=' ')
                
        print(4,2,end=' ')

        for num in range(6,n+1,2):
            print(num,end=' ')
