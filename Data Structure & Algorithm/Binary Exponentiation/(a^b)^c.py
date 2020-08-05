m = 10000007


def power_recursive(a,b):
    a = a%m
    
    if b==0:return 1

    temp = power_recursive(a,b//2) %m
    result = (temp*temp)%m
    
    if b%2==1:
        result = (result * a)%m

    return result%m

def power(a,b):
    a = a%m
    result = 1
    while b>0:
        if b%2==1:
            result = (result * a)%m

        a = (a*a)%m
        b = b//2
        
    return result%m


for I in range(int(input())):
    a,b,c = map(int,input().split())

    temp = power(a,b)
    result = power(temp,c)

    print(result)
