n,d = map(int,input().split())
a = list(map(int,input().split()))

dic = {}
for i in range(n):
    temp = i-d
    if temp<0:
        temp+=n
    dic[temp]=a[i]

for i in range(n):
    print(dic[i],end=' ')
    
