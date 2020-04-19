n,m = map(int,input().split())
a = input()
b = input()

try:
    temp=a.index("*")
except:
    temp=0

if temp==0:
    if a==b:
        print('YES')
    else:
        print('NO')

else:
    if a[:temp]==b[:temp]:
        b=b[temp:]
        l=len(a[temp+1:])

        if (b[len(b)-l:]==a[temp+1:]):
            print('YES')
        else:
            print('NO')
    else:
        print('NO')

        
