n=int(input())
k=int(input())
a=int(input())
b=int(input())
count=0
    
if k==1:
    count+=(n-1)*a
    n=1
else:
    while n>1:
        if n%k==0:
            temp=n//k
            if (n-temp)*a<b:
                count+=(n-temp)*a
                n=temp
            else:
                count+=b
                n=temp
        else:
            temp=(n//k)*k
            count+=(n-temp)*a
            n=temp

if n==0:
    count-=a

print(count)
