n,m=map(int,input().split())

a=list(map(int,input().split()))
b=list(map(int,input().split()))

evenn=0;oddn=0;evenm=0;oddm=0
for i in a:
     if i%2==0:evenn+=1
     else:oddn+=1
for i in b:
     if i%2==0:evenm+=1
     else:oddm+=1

print(min(evenn,oddm)+min(evenm,oddn))
          
