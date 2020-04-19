for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))

    temp = [0 for i in range(n+1)]

    count = 0; flag=''
    
    for i in range(n):
        temp[a[i]]+=1
        if temp[a[i]]==2:
            count+=1

        if temp[a[i]]==3:
            flag='not possible'

    for i in range(1,n-count+1):
        if temp[i]==0:
            flag='not possible'
            
        if i>count and temp[i]==2:
            flag='not possible'
            

        if i<=count and temp[i]!=2:
            flag='not possible'
        
    if flag=="":
        target = (count*(count+1))//2
        
        temp1 = 0
        for i in range(count):
            temp1 += a[i]

        temp2 = 0
        for i in range(n-1,n-count-1,-1):
            temp2+=a[i]


        if temp1==temp2 and temp1==target:
            if count==n-count:
                print(1)
                print(count,count)
            else:
                print(2)
                print(count,n-count)
                print(n-count,count)
        elif temp1==target and temp2!=target:
            print(1)
            print(count,n-count)
        elif temp2==target and temp1!=target:
            print(1)
            print(n-count,count)
        else:
            print(0)
    else:
        print(0)
    
