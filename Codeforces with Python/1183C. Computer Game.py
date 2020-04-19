for _ in range(int(input())):
    n,k,a,b=map(int,input().split())
    flag='all'
    left=0;right=k
    count=1
    while(left<=right):
        count+=1
        mid=(left+right)//2
        if n-((a*mid)+(b*(k-mid)))>0:
            left=mid+1
        else:
            right=mid-1

    print(right)
