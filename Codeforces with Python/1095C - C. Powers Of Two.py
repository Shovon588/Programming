from math import log2 as log

n,k=map(int,input().split())

result=[]

if n%2==1:
    result.append(1)
    n-=1;k-=1
    #print(n,k)

while n>0 and k>0:
    temp=int(log(n))
    j=0
    
    if n>k:
        while(j<=n):
            flag=pow(2,temp-j)
            j+=1
            
            if n-flag>=k-1:
                result.append(flag)
                n-=flag;k-=1
                break
                #print(n,k)

    else:
        break


if n==k:
    print('YES')
    for i in range(len(result)):
        print(result[i],end=' ')
    for i in range(n):
        print(1,end=' ')
else:
    print('NO')
