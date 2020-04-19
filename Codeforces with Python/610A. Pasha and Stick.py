n=int(input())
if n<6 or n%2==1:print(0)
elif n%4==0:print(((n//2)//2)-1)
else:print((n//2)//2)
