for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    
    if n==1:
        print(abs(a[0]-a[1]))
    else:
        n = (2*n)-1
        n = n//2

        print(abs(a[n]-a[n+1]))
