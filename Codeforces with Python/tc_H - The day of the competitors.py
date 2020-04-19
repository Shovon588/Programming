t=int(input())
for _ in range(t):
    n=int(input())
    count=0
    for i in range(n):
        a=list(map(int,input().split()))
        if 1 in a:
            count+=1

    print(count)
