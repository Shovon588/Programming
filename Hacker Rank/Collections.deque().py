n = int(input())

result = []
for i in range(n):
    a = list(map(str,input().split()))

    if len(a)==2:
        if a[0]=='append':
            result.append(int(a[1]))
        else:
            result.insert(0,int(a[1]))
    else:
        if a[0]=='pop':
            result.pop()
        else:
            result.remove(result[0])

for i in range(len(result)):
    print(result[i],end=' ')
