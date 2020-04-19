a,b,c=map(int,input().split())

week=0
while(1):
     if a>=3 and b>=2 and c>=2:
          week+=1;a-=3;b-=2;c-=2
     else:break

