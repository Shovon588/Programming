s=input()

if ('ba' in s) or ('cb' in s) or ('ca' in s) or ('ac' in s):
    print('NO')
else:
    a=s.count('a')
    b=s.count('b')
    c=s.count('c')

    if a==c or b==c:
        print('YES')
    #elif a==c and b==c:
        #print('YES')
    else:
        print('NO')
