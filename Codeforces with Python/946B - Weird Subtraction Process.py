a,b=input().split()
a,b=int (a),int(b)

while a>0 and b>0:
    if a>=b+b:
        a=a%(b+b)
    elif b>=a+a:
        b=b%(a+a)
    else:
        break

print (a,b)
