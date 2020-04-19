from math import ceil

n,t=map(int,input().split())

a=[]
for i in range(n):
     s,d=map(int,input().split())

     while s<t:s+=d
     a.append(s)
print(a.index(min(a))+1)
