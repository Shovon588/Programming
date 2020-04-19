start, end ,k=map(int,input().split())

count=0
for i in range(start,end+1):
    first = i
    second = int(str(i)[::-1])

    temp = abs(first-second)
    if temp%k==0:
        count+=1
    
print(count)
