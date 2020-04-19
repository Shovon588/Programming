from math import ceil

for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))

    maxa=0;mina=10000000001;diff=-1;pos=0
    
    for i in range(n):
        if a[i]>=0:
            pos+=1
            maxa=max(maxa,a[i])
            mina=min(mina,a[i])
            if i!=n-1:
                if a[i+1]>=0:
                    diff=max(diff, abs(a[i]-a[i+1]))

    if pos==0:
        print(0,1)
    else:
        temp = ceil((maxa+mina)/2)
        res = temp-mina
        if res<diff:
            print(diff, temp)
        else:
            print(res, temp)
