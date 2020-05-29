for ii in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()

    even=0; odd=0; close=0
    for i in range(n-1):
        if abs(a[i]-a[i+1])==1:
            close+=1
        if a[i]%2==0:even+=1
        else:odd+=1
        
    if a[-1]%2==0:even+=1
    else:odd+=1

    if (even%2==0 and odd%2==0) or (even%2==1 and odd%2==1 and close>0):
        print("YES")
    else:
        print("NO")
        
    
