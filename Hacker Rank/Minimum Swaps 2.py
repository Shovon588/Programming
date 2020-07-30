import sys

n = int(input())
a = list(map(int,input().split()))

dic = {}
for i,num in enumerate(a):
    dic[num]=i+1

res = 0
for num in range(1,n+1):
    if dic[num]!=num:
        pos = dic[num]
        actual = a[num-1]
        dic[actual]=pos
        dic[num]=num
        a[num-1]=num
        a[pos-1]=actual
        res+=1
print(res)
    
