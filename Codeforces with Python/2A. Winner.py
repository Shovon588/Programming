player={}
man='';check=0;temp=[]

n=int(input())
for i in range(n):
     a,b=map(str,input().split())
     b=int(b)

     if a in player:
          player[a]+=b
          if player[a]>check:man=a;check=player[a]
     else:
          player[a]=b
          if player[a]>check:man=a;check=player[a]

for i in player:
     temp.append(player[i])
