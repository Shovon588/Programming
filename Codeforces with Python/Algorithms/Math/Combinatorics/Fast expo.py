a,b=map(int,input().split())
#a,b,m=map(int,input().split())) --- m==mod that is (a^b mod m)

b = bin(b)
b = b[2:]
print(b)
result=1
for i in range(len(b)):
    if b[i]=='0':
        result=(result*result)
        #result=(result*result)%m
    else:
        result=(result*result*a)
        #result=(result*result*a)%m
    print(result)


print (result)
