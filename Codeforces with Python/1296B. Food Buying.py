for _ in range(int(input())):
    n=int(input())

    khoroch=0
    while(n//10>0):
        temp = n//10
        khoroch+=temp*10
        n=temp+(n%10)

    khoroch+=n
    print(khoroch)    
    
