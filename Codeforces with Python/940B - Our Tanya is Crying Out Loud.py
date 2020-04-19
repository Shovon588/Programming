n = int(input())
k = int(input())
a = int(input())
b = int(input())

count=0

if k==1:
    count=(n-1)*a
else:
    while(n>1):
        if n%k==0:
            c = int ((n-(n/k))*a)
            count=count+min(c,b)
            n/=k
        else:
            count+=a
            n-=1

print (count)
