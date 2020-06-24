for I in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))

    odd = 0
    for num in a:
        if num%2==1:
            odd+=1
    oddarr=[]
    evenarr=[]
        
    if odd%2==0:
        count=2
        if odd>=2:
            for i in range(2*n):
                if a[i]%2==1 and count>0:
                    a[i]=-1
                    count-=1
                elif a[i]%2==0:
                    evenarr.append(i+1)
                elif a[i]%2==1:
                    oddarr.append(i+1)
        else:
            for i in range(2*n):
                if a[i]%2==0 and count>0:
                    a[i]=-1
                    count-=1
                elif a[i]%2==0:
                    evenarr.append(i+1)
                elif a[i]%2==1:
                    oddarr.append(i+1)
            
    else:
        odd=''
        even=''
        for i in range(2*n):
            if a[i]%2==0 and even=='':
                a[i]=-1
                even='done'
            elif a[i]%2==1 and odd=='':
                a[i]=-1
                odd='done'
            elif a[i]%2==0:
                evenarr.append(i+1)
            elif a[i]%2==1:
                oddarr.append(i+1)
                
        
    for i in range(0,len(oddarr),2):
        print(oddarr[i],oddarr[i+1])
        
    for i in range(0,len(evenarr),2):
        print(evenarr[i],evenarr[i+1])

