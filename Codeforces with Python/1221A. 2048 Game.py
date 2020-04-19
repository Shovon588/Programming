t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()

    j=0;leng=n
    for i in range(10000):
        if j>=len(a)-1:break
        if a[j]==a[j+1]:
            a.append(a[j]+a[j])
            j=j+2
            a.sort()
        else:j+=1

        

    if 2048 in a:
        print('YES')
    else:
        print('NO')
