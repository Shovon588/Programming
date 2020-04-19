n=int(input())
s=input()
t=input()

c=0;a=0;b=0;d=0
clown=[];acro=[];both=[];dudh=[]

for i in range(n):
     if s[i]==t[i]:
          if t[i]=='0':
               d+=1
               dudh.append(i+1)
          else:
               b+=1
               both.append(i+1)
               
     else:
          if s[i]=='1':
               c+=1
               clown.append(i+1)
          else:
               a+=1
               acro.append(i+1)

#print('C A B D')
#print(c,a,b,d)

if c==a:
     if b%2==1 or d%2==1:
          print(-1)
     else:
          print(*clown,end='')
          for i in range(b//2):
               print(both[i],end=' ')
          for i in range(d//2):
               print(dudh[i],end=' ')
