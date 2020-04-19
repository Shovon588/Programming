n=int(input())


for i in range(n):
    b=[]
    if i==0:
        a=list(map(int,input().split()))
        temp=a[1:]
    else:
        a=list(map(int,input().split()))
        a=a[1:]

        for i in range(len(a)):
            if a[i] in temp:
                b.append(a[i])

        temp=b

print(*temp)
