n=int(input())
m=int(input())
a=int(input())
b=int(input())
total=int(input())

temp=(n*(a-1))+(m*(b-1))


if temp>=total:
    mini=0
else:
    temp=total-temp
    if temp>=n+m:
        mini=n+m
    else:
        mini=(n+m)-temp


if a>=b:
    temp=total//b
    if temp>=m:
        temp=m
        total-=temp*b
    else:
        total-=temp*b
    maxi=temp

    temp=total//a
    if temp>=n:
        temp=n
        total-=temp*a
    else:
        total-=temp*a

    maxi+=temp
else:
    temp=total//a
    if temp>=n:
        temp=n
        total-=temp*a
    else:
        total-=temp*a

    maxi=temp

    temp=total//b
    if temp>=m:
        temp=m
        total-=temp*b
    else:
        total-=temp*b

    maxi+=temp

print(mini,maxi)
