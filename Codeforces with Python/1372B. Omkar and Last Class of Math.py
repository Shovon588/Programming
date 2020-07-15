from math import gcd, sqrt


def compute_lcm(x, y):
   lcm = (x*y)//gcd(x,y)
   return lcm

for I in range(int(input())):
    n = int(input())

    mini = 10000000000000
    res = [-1,-1]
    for i in range(1,int(sqrt(n))+2):
        if n%i==0:
            if n-i>0:
                lcm = compute_lcm(i,n-i)
                if lcm<mini:
                    mini = lcm
                    res = [i,n-i]
            
            temp = n//i
            if n-temp>0:
                lcm = compute_lcm(temp,n-temp)
                if lcm<mini:
                    mini = lcm
                    res = [temp,n-temp]

    print(*res)
