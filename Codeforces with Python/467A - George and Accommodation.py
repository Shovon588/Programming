n=int(input())

count=0
for i in range (n):
    a,b = input().split()

    a,b=int (a), int (b)

    if b-a>=2:
        count+=1

print (count)
