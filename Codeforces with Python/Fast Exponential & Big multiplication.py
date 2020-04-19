m=1000000000000037

def mul1(a,b,mod):
    result=0
    while(b>0):
        if b%2!=0:
            result+=a
            result=result%mod
            
        b=b//2
        a=(2*a)%mod
    return result

def mul2(a,b,mod):
    result=0
    while(b>0):
        if b%2!=0:
            result+=a
            result=result%mod
            
        b=b//2
        a=(2*a)%mod
    return result

def fastExpo1(b,p):
    result=1
    while(p>0):
        if p%2!=0:
            result=mul1(result,b,m-1)
        p=p//2
        b=mul1(b,b,m-1)

    return result

def fastExpo2(b,p):
    result=1
    while(p>0):
        if p%2!=0:
            result=mul2(result,b,m)
        p=p//2
        b=mul2(b,b,m)

    return result


a,b,c=map(int,input().split())


res=fastExpo1(b,c)

result=fastExpo2(a,res)

print(result)
