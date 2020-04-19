n=int(input())
a=n//10
b=(a*10)-1
c=n-b
sum=0
while (b != 0):
        rem=b%10
        sum=sum+rem
        b=b//10
while (c != 0):
        rem=c%10
        sum=sum+rem
        c=c//10
print(sum)
