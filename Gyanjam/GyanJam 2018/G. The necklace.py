t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    
    start=0;val=a[0];count=0;result=0
    
    for j in range(n):
        if a[start]==-1:
            count=0

            for k in range(n):
                 if a[k]!=-1:
                    start=k;val=a[k]

        a[start]=-1
        start=val
        val=a[start]
        count+=1
        
        if count>result:
                result=count

    print('Case %d: %d'%(i+1,result))
        
