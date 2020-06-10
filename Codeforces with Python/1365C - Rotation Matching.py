n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

pos = {}

for i in range(n):
    pos[a[i]]=i

dic = {}
for i in range(n):
    cur = pos[b[i]]-i
    if cur<0:
        cur+=n

    if cur in dic:
        dic[cur]+=1
    else:
        dic[cur]=1

res = 0
for key, value in dic.items():
    res = max(res,value)
print(res)
