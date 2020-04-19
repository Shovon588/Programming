t = int(input())

for z in range(t):
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse=True)

    tot = 0
    flag=''
    for i in range(n):
        tot+=a[i]

        if tot//(i+1)>=x:
            continue
        else:
            flag='last er  ta bad'
            break
        
    if flag=="":
        print(i+1)
    else:
        print(i)
