from math import sqrt as root

while(1):
    try:
        a,b,c=map(int,input().split())

        s=(a+b+c)/2
        ans = (4 * root(s*(s-a)*(s-b)*(s-c))) / 3

        if ans>0:
            print("%.3f" %ans)
        else:
            print('-1.000')
        
    except EOFError:
        break
