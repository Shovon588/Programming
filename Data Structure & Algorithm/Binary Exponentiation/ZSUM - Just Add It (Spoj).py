"""
Final Eq: 2*(n-1)^k + n^k + 2*(n-1)^(n-1) + n^n
So, need to calculate:
1. (n-1)^k
2. n^k
3. (n-1)^(n-1)
4. n^k
"""
m = 10000007
def power(a,b):
    """
    This is an iterative function that computes a^b
    """
    a = a%m
    result = 1
    while b>0:
        if b%2==1:
            result = (result * a) % m

        a = (a*a) %m
        b = b//2
        
    return result%m

while True:
    n,k = map(int,input().split())
    if n+k==0:break

    arr = []
    arr.append((power(n-1,k)*2)%m)
    arr.append(power(n,k))
    arr.append((power(n-1,n-1)*2)%m)
    arr.append(power(n,n))

    result = 0
    for num in arr:
        result = (result+num)%m

    print(result)
    
