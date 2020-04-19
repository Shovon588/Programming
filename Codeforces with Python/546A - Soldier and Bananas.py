k,n,w = input().split()

k,n,w = int (k),int (n), int (w)
money=0

for i in range (1,w+1):
   money+=(i*k)

if money>n:
    print (money-n)
else:
    print (0)
