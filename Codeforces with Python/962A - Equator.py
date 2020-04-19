n=int(input())
a=list(map(int,input().split()))
b=sum(a)/2

i=0;k=0

while k<b:
    k+=a[i]
    i+=1
print (i)
