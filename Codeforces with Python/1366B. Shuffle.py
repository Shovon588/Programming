for I in range(int(input())):
    n,x,m = map(int,input().split())

    left = x
    right = x

    for i in range(m):
        l,r = map(int,input().split())
        
        if l<=left and r>=left:
            left=min(left,l)
            right=max(right,r)

        if r>=right and l<=right:
            left=min(left,l)
            right=max(right,r)

    print(right-left+1)
