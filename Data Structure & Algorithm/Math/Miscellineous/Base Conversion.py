n=int(input())

res=''
while(n>0):
     if n%8==0:
          res+='0'
          n=n//8
     else:
          temp=n%8
          res+=str(temp)
          n=n//8
