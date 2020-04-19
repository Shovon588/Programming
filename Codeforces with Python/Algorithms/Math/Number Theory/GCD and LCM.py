a,b=map(int,input().split())

def gcd(a,b):
    if a%b==0:return b
    else:return gcd(b,a%b)

g=gcd(a,b)
print('GCD=',g)

l=(a*b)//g #a*b=g*l
print('LCM=',l)
