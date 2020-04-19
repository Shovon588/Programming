n,m=map(int,input().split())

count=0
while(m>n):
    if m%2==0:
        m=m//2
        count+=1
    else:
        m+=1
        count+=1

count+=(n-m)
print(count)
