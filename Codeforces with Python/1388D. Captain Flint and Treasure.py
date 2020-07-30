n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

giving = {}
getting = {}

for i in range(n):
    if b[i]!=-1:
        giving[i+1] = b[i]
        getting[b[i]] = i+1

