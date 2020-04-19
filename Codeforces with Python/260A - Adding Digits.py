a,b,n=map(int,input().split())

for _ in range(1):
    flag='no'
    for i in range(10):
        temp=str(a)+str(i)
        if int(temp)%b==0:
            a=temp
            flag='yes'
            break

if flag=='no':print(-1)
else:
    a=a+('0'*(n-1))
    print(a)
