n = int(input())

a = list(map(int,input().split()))

b = a.count(2)
c = a.count(3)
d = a.count(4)

temp = sum(a)
count=0
while(1):
    if temp/n>=4.5:
        break
    elif b>0:
        b-=1
        temp+=3
        count+=1
    elif c>0:
        c-=1
        temp+=2
        count+=1
    elif d>0:
        d-=1
        temp+=1
        count+=1

print(count)
