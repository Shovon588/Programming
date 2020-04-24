from sys import stdin, stdout

input = stdin.buffer.readline

t=int(input())
for _ in range(t):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))

    dic={}
    maxi=0;mini=1000000005
    for i in range(n//2):
        temp = a[i]+a[n-i-1]
        try:
            if dic[temp]:
                dic[temp]+=1
        except KeyError:
            dic[temp]=1
            
        maxi=max(maxi,a[i])
        mini=min(mini,a[i])

    mini+=k;maxi+=1
    mini,maxi=min(mini,maxi),max(mini,maxi)
    
    lar=0;val=-1
    for i in range(mini,maxi+1):
        try:
            if dic[i]:
                if dic[i]>lar:
                    lag=dic[i]
                    val=i
        except KeyError:
            pass
        
    if val==-1:
        target=mini
    else:
        target=val

    
    count=0
    for i in range(n//2):
        if a[i]+a[n-i-1]!=target:
            count+=1

    stdout.write(str(count)+'\n')

    '''
    dic = {}
    for i in range(n//2):
        temp = a[i]+a[n-i-1]
        try:
            if dic[temp]:
                dic[temp]+=1
        except KeyError:
            dic[temp]=1
    '''
