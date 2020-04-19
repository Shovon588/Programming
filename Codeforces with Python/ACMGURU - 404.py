m,n = input().split()

m,n = int (m), int (n)

a=[]
for i in range (n):
    a.append(input())

b = (m//n)+1
a=a*b

print (a[m-1])
