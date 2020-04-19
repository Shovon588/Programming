from math import ceil

for _ in range(int(input())):
    a=input()
    b=input()
    c=input()

    okay=0
    for i in range(len(a)):
        if a[i]==c[i] or b[i]==c[i]:
            okay+=1

    if okay==len(a):
        print('YES')
    else:
        print('NO')
    
