n = int (input())

x=0;y=0;z=0;
for i in range (n):
    a,b,c = input().split()

    a,b,c = int (a), int (b), int (c)
    x+=a
    y+=b
    z+=c

if x==0 and y==0 and z==0:
    print ("YES")
else:
    print ("NO")
