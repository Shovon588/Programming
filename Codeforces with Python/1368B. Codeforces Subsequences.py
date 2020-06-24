from math import sqrt

n = int(input())

m = sqrt(n)
m = int(sqrt(m))

arr = [m for i in range(4)]

tot = 1
for num in arr:
    tot = tot*num

i=3
while(tot<n):
    arr[i]+=1
    i-=1
    tot = tot//m
    tot = tot*(m+1)

print("c",end='')
print("o"*arr[0],end='')
print("d",end='')
print("e"*arr[1],end='')
print("f",end='')
print("o"*arr[2],end='')
print("rc",end='')
print("e"*arr[3],end='')
print("s")
