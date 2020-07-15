n = int(input())
a = list(map(int,input().split()))

count = 0
for i,num in enumerate(a):
    if (i+1)%2==1 and num%2==1:
        count+=1


print(count)

