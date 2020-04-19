n=int(input())
a=list(map(int,input().split()))

count=1
temp=a[0]
track=[]
for i in range(1,n):
     if a[i]==temp:
          count+=1
     else:
          temp=a[i]
          track.append(count)
          count=1
track.append(count)

temp=len(track)

count=0
for i in range(temp-1):
     if min(track[i],track[i+1])*2>count:
          count=min(track[i],track[i+1])*2
print(count)
