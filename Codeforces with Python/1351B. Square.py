from math import sqrt as s

for _ in range(int(input())):
    a,b = map(int,input().split())
    c,d = map(int,input().split())
    a,b = max(a,b),min(a,b)
    c,d = max(c,d),min(c,d)
    total = a+b+c+d

    temp = -1
    if a==c:
        total = total-a-c
        temp=a
    elif a==d:
        total = total-a-d
        temp=a
    elif b==c:
        total = total-b-c
        temp=b
    elif b==d:
        total = total-b-d
        temp=b


    if total==temp:
        print('YES')
    else:
        print('NO')
