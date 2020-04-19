t=int(input())
for _ in range(t):
    dig=[];temp=[];zero=0
    n=int(input())
    a=list(map(int,input().split()))
    for i in range(n-1):
        if a[i]==0:zero+=1
        elif a[i]==a[i+1]:
            dig.append(a[i]*2)
            a[i+1]=0
        else:dig.append(a[i])
                
    if i+1<n and a[i+1]>0:
        dig.append(a[i+1])
    elif i+1<n and a[i+1]==0:
        zero+=1

    dig=dig+[0]*zero
    l=len(dig)
    for i in range(l):
        print(dig[i],end=' ')
    print()
