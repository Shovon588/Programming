n=int(input())
a=list(map(int,input().split()))
x=(1<<29);count=0;suma=0

for i in range(len(a)):
    if a[i]<0:
        count+=1
        a[i]=a[i]*-1
    suma=suma+a[i]
    b=min(x,suma)


if count%2==0 and n%2!=0:
    suma-=2*x

print(suma)
