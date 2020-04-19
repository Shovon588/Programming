from math import sqrt as s


def factorization(n):
    a=[]
    while n%2==0:
        a.append(2)
        n = n//2

    for i in range(3,int(s(n))+1,2):
        while n%i==0:
            a.append(i)
            n = n//i
                    
    if n>2:
        a.append(n)
    return a

for i in range(int(input())):
    n = int(input())
    a = factorization(n)

    flag='hobe'
    
    if len(a)<3:
        flag='miao'
    else:
        res = []
        res.append(a[0])

        if a[1]==a[0]:
            res.append(a[1]*a[2])
            j=3
        else:
            res.append(a[1])
            j=2

        temp=1
        for i in range(j,len(a)):
            temp=temp*a[i]
            
        if temp in res or temp==1:
            flag='miao'
        else:
            res.append(temp)

    if flag=='miao':
        print('NO')
    else:
        print('YES')
        print(*res)
