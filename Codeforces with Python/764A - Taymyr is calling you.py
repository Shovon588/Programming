a,b,n = input().split()
a,b,n= int(a), int (b), int (n)

c=[]; d=[];
for i in range(1,n+1):
    f=i*a
    g=i*b

    if f>n and g>n:
        break;
    else:
        c.append(i*a)
        d.append(i*b)

e=set(c) & set(d)
print (len(e))
