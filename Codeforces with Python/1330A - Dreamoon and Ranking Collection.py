for _ in range(int(input())):
    n, x = map(int,input().split())
    a = list(map(int,input().split()))
    temp = [0 for i in range(210)]

    for i in range(n):
        temp[a[i]]+=1

    for i in range(1,210):
        if temp[i]==0:
            x-=1

        if x==0:
            break
    
    res = i
    for j in range(i+1,210):
        if temp[j]==0:
            break
        else:
            res+=1
    print(res)
