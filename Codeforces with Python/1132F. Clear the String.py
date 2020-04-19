n=int(input())
s=input()

temp={}
for i in s:
     if i in temp:
          temp[i]+=1
     else:
          temp[i]=1
