p,q = map(int,input().split())

flag=''
for i in range(p,q+1):
    sq = i*i
    temp = str(sq)
    leni = len(str(i))
    lensq = len(temp)

    l = '0'
    r = temp[-leni:]
    if leni!=lensq:
        l = temp[:lensq-leni]

    num = int(l)+int(r)

    if num==i:
        flag='done'
        print(i, end=' ')

if flag=='':
    print('INVALID RANGE')
    
    
