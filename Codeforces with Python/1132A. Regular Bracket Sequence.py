a=int(input())
b=int(input())
c=int(input())
d=int(input())

left=(2*a)+b+c
right=(2*d)+c+b

if left==right and left+right!=2:print(1)
else:print(0)
