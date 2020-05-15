for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))

    alice = 0
    bob = 0
    ai = 0
    bi = n-1
    alicepre = 0
    bobpre = 0
    count=0
    
    while ai<=bi:
        aliceeaten='no';bobeaten='no'
        
        if alicepre<=bobpre:
            for i in range(ai,bi+1):
                if aliceeaten=='no':
                    # print('alice')
                    count+=1
                    aliceeaten='yes'
                alicepre+=a[i]
                alice+=a[i]
                ai=i+1
                
                if alicepre>bobpre:
                    bobpre=0
                    break

        if bobpre<=alicepre:
            for i in range(bi,ai-1,-1):
                if bobeaten=='no':
                    # print('bob')
                    count+=1
                    bobeaten='yes'
                    
                bobpre+=a[i]
                bob+=a[i]
                bi=i-1
                if bobpre>alicepre:
                    alicepre=0
                    break

    print(count,alice,bob)
