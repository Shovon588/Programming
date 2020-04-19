
n=int(input())
a=[]
for i in range(n):
    b=input()
    a.append(b)


def Sorting(lst):
    lst2 = sorted(lst, key=len)
    return lst2

b=Sorting(a)

count=1
for i in range(n-1):
    if b[i] in b[i+1]:
        count+=1

if count==n:
    print('YES')
    for i in range(n):
        print(b[i])
else:
    print('NO')
