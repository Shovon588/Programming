check=['First','Second','Third']
t=int(input())
for i in range(t):
    a=list(map(int,input().split()))
    temp=a.index(min(a))
    print(check[temp])
