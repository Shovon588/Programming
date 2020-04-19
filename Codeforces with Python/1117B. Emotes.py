n,m,k=map(int,input().split())
a=list(map(int,input().split()))

a.sort(reverse=True)

num1=a[0];num2=a[1]

count=0;res=0
res+=((m//(k+1))*num2)
res+=((m-(m//(k+1)))*num1)

print(res)
