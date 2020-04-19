a,b,n=map(int,input().split())
import math

def bSearch(n):
    a=[10,20,30,40,50,60,70,80,90,100,110,120]

    low=0; high=len(a)-1;
    index= -1

    while low<=high:
        mid=int((high+low)/2)

        if a[mid]==n:
            index=mid
            break
        elif a[mid]<n:
            low=mid+1
        else:
            high=mid-1

    if index==-1:
        print('bSearch --> The number is not in the list')
    else:
        print('bSearch --> The number is in ',index,' th index')


def fastExpo(a,b,n):
    b=bin(b)
    b=b[2:]
    result=1

    for i in range(len(b)):
        if b[i]=='0':
            result=(result*result)%n
        else:
            result=(a*result*result)%n

    print('fastExpo --> The result is: ',result)


def pSieve(n):
    a=[True for i in range(n+1)]
    p=2
    b=[]

    while p*p<=n:
        if a[p]==True:
            for i in range(2*p,n+1,p):
                a[i]=False

        p+=1

    for i in range(2,n+1):
        if a[i]:
            b.append(i)

    print ('Sieve list is: ',b,end=' ')
    print()


def pFact(n):
    c=[]
    while n%2==0:
        c.append(2)
        n=int(n/2)

    for i in range(3,int(math.sqrt(n))+1,2):
        while n%i==0:
            c.append(i)
            n=int(n/i)

    if n>2:
        c.append(n)

    print('pFact --> The result is: ',c,end=' ')
    
bSearch(n)
fastExpo(a,b,n)
pSieve(n)
pFact(n)
