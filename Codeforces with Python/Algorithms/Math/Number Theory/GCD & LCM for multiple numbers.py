a=list(map(int,input().split()))
first=a[0]

def gcd(first,last):
    if first%last==0:return last
    else:return gcd(last,first%last)
    
for i in range(1,len(a)):
    last=a[i]
    g=gcd(first,last)
    
    l=(first*last)//g
    first=g


print('GCD & LCM of above numbers are',g,'and',l)

    
        
