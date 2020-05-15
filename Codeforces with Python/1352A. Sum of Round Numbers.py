for _ in range(int(input())):
    n = input()
    l = len(n)

    if n.count('0')==len(n)-1:
        print(1)
        print(n)
    else:
        res = []
        count=0
        for i in range(l):
            if n[i]!='0':
                temp = n[i]+('0'*(l-i-1))
                res.append(temp)
                count+=1
        print(count)
        print(*res)
