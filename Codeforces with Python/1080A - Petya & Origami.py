n,k=map(int,input().split())

red=2*n
green=5*n
blue=8*n

total=0
if red%k==0:
    total+=red//k
else:
    total+=(red//k)+1

if green%k==0:
    total+=green//k
else:
    total+=(green//k)+1

if blue%k==0:
    total+=blue//k
else:
    total+=(blue//k)+1

print(total)
