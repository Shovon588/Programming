from sys import stdin, stdout

#input = stdin.buffer.readline
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))

    dic = {}
    maxi = 0
    unique = -1
    for num in a:
        try:
            if dic[num]:
                dic[num]+=1
                maxi = max(maxi,dic[num])
        except KeyError:
            dic[num]=1
            unique+=1
            maxi=max(maxi,1)

    
    if unique>=maxi:
        res = maxi
    else:
        unique+=1
        maxi-=1
        res = min(maxi,unique)

    stdout.write(str(res)+'\n')
