n,t=map(int,input().split())

s=input()

p=s.index('.')

frac=s[p+2:]


for i in range(len(frac)):
     if int(frac[i])>=5:
          temp=i
          break
else:temp=0

if temp>=1:
     for i in range(t):
          frac=frac[:temp-1]+str(int(frac[temp-1])+1)
          

          if int(frac[-1])<5:break
          temp-=1

          if temp<1:break



if len(frac)==0:
     print(s[:p+2])
elif int(frac[-1])>=5 and i<t-1:
     print(s[:p+1]+str(int(s[p+1])+1))
else:
     print(s[:p+1]+s[p+1]+frac[:temp+1])
     


'''
if int(frac[-1])>=5 and i<t-1:
     print(s[:p+1]+str(int(s[p+1])+1))
else:
     print(s[:p+1]+s[p+1]+frac[:temp+1])

'''
#print(s[:p+1]+frac[:temp+1])

