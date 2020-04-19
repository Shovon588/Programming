n=int(input())
dic={}


while(1):
     if n in dic:
          break
     else:
          dic[n]=1
     n+=1

     if n%10==0:
          while n%10==0:
               n=n//10
print(len(dic))
