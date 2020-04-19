n = int(input())
a = list(map(int,input().split()))


dic = {}

dic['yo']=0

ran=1
brk=1

for i in range(n):
    num=a[i]
    for key in dic:
        print(key)
