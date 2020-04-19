n = int(input())
check=[0]*(pow(10,5)+5)
a = list(map(int,input().split()))
b=set(a)

if 0 in a:
    print(len(b)-1)
else:
    print(len(b))
