from math import sqrt as s
n=int(input())
m=int(s(n))+1

flag=''
for i in range(m,0,-1):
    if n%i==0:
        flag='hmm'
        j=n//i
        break

if n==1:
    print(4)
else:
    print(2*(i+j))
