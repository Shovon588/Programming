for _ in range(int(input())):
    n = int(input())
    a=[]

    for i in range(n):
        b,c = map(int,input().split())
        a.append((b,c))
    a.sort()

    cx=0;cy=0;string='';flag='hobe'

    for x,y in a:
        if cx<=x:
            string+=('R'*(x-cx))
            cx=x
        else:
            flag='miao'
            break

        if cy<=y:
            string+=('U'*(y-cy))
            cy=y
        else:
            flag='miao'
            break

    if flag=='miao':
        print('NO')
    else:
        print('YES')
        print(string)
    
