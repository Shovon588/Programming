t=int(input())

while t>0:
    a,b=input().split()
    b=int(b)
    c=''.join(set(a))
    len1=len(a)
    len2=len(c)

    if len1-len2<=b:
        print('YES')
    else:
        print('NO')

    t-=1
