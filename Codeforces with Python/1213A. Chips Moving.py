n=int(input())
a=list(map(int,input().split()))

even=0;odd=0
for i in a:
    if i%2==0:
        even+=1
    else:
        odd+=1

print(min(even,odd))
    
