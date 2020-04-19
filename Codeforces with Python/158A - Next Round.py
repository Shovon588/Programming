n,k = input().split()

n,k = int (n), int (k)

a=list(map(int,input().split()))

count=0
if a[0]==0:
    print (count)
else:
    for i in range(n):
        if a[i]>=a[k-1] and a[i]!=0:
            count+=1
        else:
            break
    print (count)
