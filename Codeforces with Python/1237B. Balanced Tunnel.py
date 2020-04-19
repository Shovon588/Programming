n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))


enter={};ber={}

for i in range(n):
    enter[a[i]]=i+1

for i in range(n):
    ber[b[i]]=enter[b[i]]
    
