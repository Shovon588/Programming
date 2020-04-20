n=int(input())


#-------------------------------Derengement number-------------------------------
def Derengement(n):
    if n==0:return 1
    if n==1:return 0
    if n==2:return 1
    return (n-1)*(Derengement(n-2)+Derengement(n-1))

print('Derengement number of',n,'=',Derengement(n))


#During recursion the same value doesn't repeat!
def Derengement_Efficient(n):
    a=[0 for i in range(n+1)]
    a[0],a[1],a[2]=1,0,1
    for i in range(3,n+1):
        a[i]=(i-1)*(a[i-1]+a[i-2])
    return a[n]

print('Derengement number of',n,'in efficient method=',Derengement_Efficient(n))

#Details about derengement number
#https://www.geeksforgeeks.org/count-derangements-permutation-such-that-no-element-appears-in-its-original-position/
#http://oeis.org/wiki/Number_of_derangements

#-------------------------------Catalan number-------------------------------------

def catalan(n):
    a=[0 for i in range(n+1)]
    a[0],a[1]=1,1

    for i in range(2,n+1):
        a[i]=0
        for j in range(i):
            a[i]=a[i]+(a[j]*a[i-j-1])

    return a[-1]
print(n,'th catalan number is',catalan(n))

#Details about catalan number
#https://www.geeksforgeeks.org/program-nth-catalan-number/
#http://mathworld.wolfram.com/CatalanNumber.html


#----------------------------------Fibonacchi number------------------------------------------

def fibo(n):
        a=[0 for i in range(n+1)]
        a[0],a[1]=0,1
        for i in range(2,n+1):
            a[i]=a[i-1]+a[i-2]
            
        return a[-1]
    
print(n,'th fibonacci number =',fibo(n))
