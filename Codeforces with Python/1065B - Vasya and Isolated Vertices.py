v,e=map(int,input().split())
min=(max(0,v-2*e))

n=0
while(n*(n-1)//2)<e:
      n+=1
max=v-n
print(min,max)
