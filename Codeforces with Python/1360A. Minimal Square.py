for i in range(int(input())):
    a,b = map(int,input().split())
    mini = min(2*a,2*b)
    maxi = max(a,b)
    print(pow(max(mini,maxi),2))
