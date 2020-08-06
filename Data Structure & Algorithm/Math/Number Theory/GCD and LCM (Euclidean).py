a,b=map(int,input().split())

def gcd_recursive(a,b):
    if b==0:
        return a

    return gcd(b, a%b)



def gcd_iterative(a,b):
    while b>0:
        a = a%b
        a,b = b,a

    return a


def lcm(a,b):
    result = (a*b)//gcd_iterative(a,b)
    return result
