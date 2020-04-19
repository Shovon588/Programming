for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))

    flag='Yes'
    left=0;right=n-1
    while(left<right):
        maxi = max(a)
        if a[left]==maxi:
            a[left]=-1
            left+=1
        elif a[right]==maxi:
            a[right]=-1
            right-=1
        else:
            flag='No'
            break
        print(left,right)
    print(flag)
        
