n = int(input())

check=0
if n<4:
    check=1
    print('No')
elif n%4==0 or n%7==0:
    check=1
    print('Yes')
else:
    while n>7:
        n-=7
        if n%4==0:
            check=1
            print('Yes')
            break

if check==0:
    print('No')
