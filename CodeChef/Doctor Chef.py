def binsearch(m):
    left = 0
    right = n-1

    while left<=right:
        
        mid = (left+right)//2
        if a[mid]==m:
            return mid
            break
        elif a[mid]>m and a[mid-1]<m:
            return mid-1
            break
        elif a[mid]<m and a[mid+1]>m:
            return mid
            break
        elif a[mid]>m:
            right = mid-1
        else:
            left=mid+1
        

for I in range(int(input())):
    n,x = map(int,input().split())
    a = list(map(int,input().split()))

    mini = min(a)
    maxi = max(a)
    a.sort()

    count = 0
    temp = n
    while x<maxi:
        if x<mini:
            x = 2*x
        else:
            index = binsearch(x)
            if a[index]==x:
                temp-=1
                x = 2*x
                a[index]=-1
            #elif abs(x//2-a[index])>=x//4 or a[index]*2>=a[index+1]:
            elif 2*a[index]>=x:
                temp-=1
                x=a[index]*2
                a[index]=-1
            else:
                x = 2*x
                
        count+=1


    print(count+temp)











    
        
