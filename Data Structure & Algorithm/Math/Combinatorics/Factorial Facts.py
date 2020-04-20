from math import log10,floor

#n hocche je number er factorial ber korte hobe, ar p hocche n!
#er sathe p kotobar gun akare ache seita ber korar jonno

n,p=map(int,input().split())


#N! e koto gula p gun akare ache tar sonkha
def FactErPechonerZero(n,p):
    b=1;a=1;c=0
    while(1):
        a=a*p
        b=n//a
        if b>0:c+=b
        else:break
    return c
print('No of ',p,'in',n,'!=',FactErPechonerZero(n,p))



#Value of N!
def Fact_N(n):
    a=1
    for i in range(1,n+1):
        a=a*i
    return a
print('Factorial of',n,'=',Fact_N(n))


#Value of N! using DP
def Fact_N(n):
    a=[0 for i in range(n+1)]
    a[0]=1
    for i in range(1,n+1):
        a[i]=a[i-1]*i
        print(a[i])
    return a[-1]




#N! a total koto gula digit ache segula ber korar jonno
def digitOfFact(n):
    a=0
    for i in range(1,n+1):
        a=a+log10(i)
        
    a=floor(a)
    a+=1
    return a
print('No of digits in',n,'factorial is',digitOfFact(n))


#n tomo triangle number
def triangleNumber(n):
    a=(n*(n+1))//2
    return a

print(n,'th trianlge number is',triangleNumber(n))

#Triangle number hocche sei number jeta dia ekta triangle banano jai
#Ex: 1,3,6,10,15,21,28,36 (first 8 triangular number)




#For more: http://alavolacoder.blogspot.com/2013/04/factorial-facts.html
