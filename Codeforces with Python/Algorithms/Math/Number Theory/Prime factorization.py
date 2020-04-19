import math
n = int(input())
a=[]

while n%2==0:
    #print (2,end=' ')
    a.append(2)
    n = n//2

for i in range(3,int(math.sqrt(n))+1,2):
    while n%i==0:
        a.append(i)
        n = n//i
                
if n>2:
    a.append(n)
