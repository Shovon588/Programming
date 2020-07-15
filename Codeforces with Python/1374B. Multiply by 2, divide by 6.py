for I in range(int(input())):
    n = int(input())

    res = 0
    while(1):
        if n==6:
            n = n//6
            res+=1
            break
        
        if n%6==0:
            if (n//6)%6==0:
                n = n//6
            else:
                if ((n*2)//6)%6==0:
                    n = n*2
                else:
                    break
        else:
            if (n*2)%6==0:
                n = n*2
            else:
                break
        res+=1

    if n!=1:
        print(-1)
    else:
        print(res)
