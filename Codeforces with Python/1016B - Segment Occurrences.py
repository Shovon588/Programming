n,m,q = map(int,input().split())
s = input()
t = input()

for i in range(q):
    a,b = map(int,input().split())
    temp=s[a-1:b]
    print(temp.count(t))

