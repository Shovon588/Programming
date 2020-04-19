for i in range(int(input())):
    n=int(input())
    count=0
    while(n>1):
        if n%2==1:
            n-=1
            count+=1
        else:
            n=n//2
            count+=1

    print(count)
