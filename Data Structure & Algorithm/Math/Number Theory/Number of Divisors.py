'''from math import sqrt as s
n=int(input())
i=1;count=0


while(i<=s(n)):
    if n%i==0:
        if i==n//i:
            count+=1
        else:
            count+=2
    i+=1
print(count)'''

import math
n = int(input())
m=n
a=[]

while n%2==0:
    #print (2,end=' ')
    a.append(2)
    n = int(n/2)

for i in range(3,int(math.sqrt(n))+1,2):
    while n%i==0:
        a.append(i)
        n = int(n/i)
                
if n>2:
    a.append(n)

b=list(set(a))
temp=[]
for i in b:
    temp.append((i,a.count(i)))


NOD=1 #Number of divisors
for i in range(len(temp)):
    NOD=NOD*(temp[i][1]+1)

print('Number of divisors is:',NOD)


SOD=1 #Sum of divisors
for i in range(len(temp)):
    res=(pow(temp[i][0],temp[i][1]+1)-1)//(temp[i][0]-1)
    SOD=SOD*res
print('Sum of  divisors is:',SOD)


#Product of divisors
POD=pow(m,NOD//2)
print('Product of divisors is:',POD)


#Check the number is perfect or nor.
#If SOD-n==n then the number is perfect


if SOD-m==m:print(m,'is a perfect number.')
else:print(m,'is not a perfect number')



