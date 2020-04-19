a=int(input())

low=0;high=a;

while high-low>0.00000001:
    mid=(high+low)/2

    if mid*mid>a:
        high=mid
    else:
        low=mid


print('The square root is: ',mid)
