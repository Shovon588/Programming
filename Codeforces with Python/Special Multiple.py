t=int(input())
for _ in range(t):
    n=int(input())
    i=1
    while(1):
        a=bin(i);a=a[2:];a=a.replace('1','9');a=int(a);i+=1
        if a%n==0:
            print(a)
            break
