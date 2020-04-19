for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    n-=1

    count=0
    for i in range(1,n+1):
        pos=a.index(i);rightpos=pos-1

        while(rightpos>=0):
            if count==n:
                    break
            if a[rightpos]>a[pos]:
                a[pos],a[rightpos]=a[rightpos],a[pos]
                pos-=1;rightpos-=1;count+=1
            else:
                break
    print(*a)
