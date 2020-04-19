n,d = map(int,input().split())

a = list(map(int,input().split()))

dic = {}

for i in range(n):
    try:
        if dic[a[i]]:
            dic[a[i]]+=1
    except KeyError:
        dic[a[i]] = 1
    

count=0
for num in dic:
    try:
        if dic[num+d] and dic[num+2*d]:
            count+=dic[num]
    except KeyError:
        continue

print(count)
