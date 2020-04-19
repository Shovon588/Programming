n = int(input())
a = list(map(int,input().split()))

dic = {}

for i in range(n):
    try:
        if dic[a[i]]:
            dic[a[i]].append(i)
    except KeyError:
        dic[a[i]] = [i]


mini = 1000005
flag = ''
for i in dic:
    if len(dic[i])>1:
        temp = abs(dic[i][0]-dic[i][1])
        mini = min(mini,temp)
        flag = 'miao'

if flag=='':
    print(-1)
else:
    print(mini)
