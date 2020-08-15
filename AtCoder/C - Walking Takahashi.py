x,k,d = map(int,input().split())

need = abs(x)//d

if x>0:
    if k>=need:
        x -= need*d
        k -= need
    else:
        x -= k*d
        k = 0
else:
    if k>=need:
        x += need*d
        k -= need
    else:
        x += k*d
        k = 0
    

while x>0 and k>0:
    x-=d
    k-=1

if k%2==0:
    print(abs(x))
else:
    print(x+d)
