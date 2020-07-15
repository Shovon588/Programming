for I in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))

    if n==1:
        print(a[0])
    else:
        prev = 0
        for i,num in enumerate(a):
            if i%2==0:
                prev+=num

        resulting = [0]
        resulting.append(max(0,a[1]-a[0]))

        for i in range(1,n-1):
            if i%2==0:
                temp = a[i+1]-a[i]
                temp += resulting[i-1]
            else:
                temp = a[i]-a[i+1]
                temp += resulting[i-1]
                
            resulting.append(max(0,temp))
            
        print(prev+max(resulting))




        
        
