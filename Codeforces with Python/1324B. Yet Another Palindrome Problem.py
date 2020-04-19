for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))

    dic = {}

    for i in range(n):
        try:
            if dic[a[i]]:
                dic[a[i]].append(i)
        except:
            dic[a[i]] = [i]

    flag=''
    for num in dic:
        if flag=='bingo':
            break
        temp = dic[num]
        if len(temp)>=2:
            first = temp[0]
            last = temp[-1]
            if abs(first-last)>=2:
                for x in range(first+1,last):
                    if a[i]!=temp:
                        flag='bingo'
                        break
        
    if flag=='bingo':
        print('YES')
    else:
        print('NO')
