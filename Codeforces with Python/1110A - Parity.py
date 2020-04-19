b,k=map(int,input().split())
a=list(map(int,input().split()))

sumup=0;temp=k
for i in range(k):
    sumup+=(a[i]*pow(b,temp-1))%10000
    temp-=1
