n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

karen={};koyomi={}
for i in range(n):
    karen[a[i]]=1

for i in range(n):
    karen[b[i]]=1

yes=0;

for i in range(n):
    for j in range(n):
        temp=a[i]^b[j]
        try:
            if karen[temp]:
                yes+=1
        except KeyError:
            pass

if yes%2==0:
    print('Karen')
else:
    print('Koyomi')
