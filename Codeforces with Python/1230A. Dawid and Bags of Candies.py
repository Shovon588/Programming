a,b,c,d=map(int,input().split())

total=a+b+c+d

if total%2!=0:
    print('NO')
else:
    if a+b==(total//2):print('YES')
    elif a+c==(total//2):print('YES')
    elif a+d==(total//2):print('YES')
    elif a+b+c==(total//2):print('YES')
    elif a+b+d==(total//2):print('YES')
    elif a+c+d==(total//2):print('YES')
    elif b+c==(total//2):print('YES')
    elif b+d==(total//2):print('YES')
    elif b+c+d==(total//2):print('YES')
    elif c+d==(total//2):print('YES')
    else:
        print('NO')
