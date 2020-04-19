a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s',
   't','u','v','w','x','y','z']

for _ in range(int(input())):
    n,k=map(int,input().split())

    s=''
    for i in range(k):
        s=s+a[i]

    temp=n//k

    result=''
    for i in range(temp):
        result=result+s

    for i in range(n-(temp*k)):
        result=result+a[i]

    print(result)
