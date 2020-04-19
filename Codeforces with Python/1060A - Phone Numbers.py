n=int(input())
a=input()

b=a.count('8')

c=n//11

if b==0 or n<11:
    print(0)
elif b<=c:
    print(b)
else:
    print(c)
