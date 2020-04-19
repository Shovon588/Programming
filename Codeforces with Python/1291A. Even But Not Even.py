for _ in range(int(input())):
    n = int(input())
    s = input()

    odd=0;total=0;flag='waiting'

    for i in range(n):
        total+=int(s[i])
        if int(s[i])%2==1:
            odd+=1

        if total%2==0 and total>0 and odd%2==0 and int(s[i])%2==1:
            print(s[:i+1])
            flag='done'
            break

    if flag=='waiting':
        print(-1)
