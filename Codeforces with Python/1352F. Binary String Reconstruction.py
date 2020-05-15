typen1 = '01'*200
for _ in range(int(input())):
    n0,n1,n2 = map(int,input().split())

    res = ''
    if n0>0:
        res += '0'*(n0+1)

    if n1>0:
        if n0>0:
            res+='1'
            res+=typen1[:n1-1]
        else:
            res+=typen1[:n1+1]

    if n2>0:
        if len(res)==0 or res[-1]=='0':
            res = res[:len(res)-1]
            res = '1'+res
            res+='1'*(n2)
        else:
            res+='1'*n2

    print(res)
