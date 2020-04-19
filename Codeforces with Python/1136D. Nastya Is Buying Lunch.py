n,m=map(int,input().split())

a=list(map(int,input().split()))
hello=[-1]*500005

jinis=[];asol=[];nokol=[]
for i in range(m):
     x,y=map(int,input().split())
     jinis.append((max(x,y),min(x,y)))
     
jinis.sort(reverse=True)

for i in range(n):
     hello[a[i]]=i

for i in jinis:
     if i[0]==n:
          asol.append(i)
     else:
          nokol.append(i)


l=len(asol)
ll=len(nokol)

temp=a.index(n)
while(1):
     flag='no'

     for i in range(l):
          a[temp+1]==asol[i][1]
          a[temp],a[temp+1]=a[temp+1],a[temp]
          temp+=1
          flag='yes'

     break


#Fuck u motherfucker....fuck u all
