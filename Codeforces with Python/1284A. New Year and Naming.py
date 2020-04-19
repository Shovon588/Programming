n,m = map(int,input().split())
a = list(map(str,input().split()))
b = list(map(str,input().split()))
t = int(input())

for i in range(t):
    x = int(input())

    temp1=x;temp2=x
    if x>n:
        temp1=x%n

    print(a[temp1-1], end='')
    
    if x>m:
        temp2=x%m
    print(b[temp2-1])

    
