n,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))


res=-1;taste=0;cal=0
for i in range(n):
     taste+=a[i]
     cal+=b[i]

     if taste/cal==k:
          res=taste
     
print(res)



