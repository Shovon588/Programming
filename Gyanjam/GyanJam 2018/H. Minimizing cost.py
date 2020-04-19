from collections import Counter
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    b=a[::-1]

    count=1;temp=0;totalCount=0
    
    for j in range(1,n):
        if b[j-1]==b[j]:
            count+=1
            temp=b[j]
            print(count,temp)
        else:
            j+=count-1
            totalCount+=temp*count
            temp=b[j];count=1

        print(j)
        

