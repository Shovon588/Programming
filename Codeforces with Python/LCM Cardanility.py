from math import sqrt as s,gcd

def lcm(a,b):
    return (a*b//gcd(a,b))

while(1):
    n=int(input())
    if n==0:
        break
    else:
        temp=int(s(n))

        push=[];flag=0
        for i in range(1,temp+1):
            if n%i==0:
                push.append(i);flag+=1
                if i*i!=n:
                    push.append(n//i);flag+=1

        count=0
        for i in range(flag):
            for j in range(i,flag):
                if lcm(push[i],push[j])==n:
                    count+=1

        print(n,count)
