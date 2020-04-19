h,m=map(int,input().split())

if h==12:h=0
if m==12:m=0

temp=m%5

flag=abs(h-(m-temp))
flag=(flag*6)+(temp*6)

flag=flag-((.5*m))
print(flag)
