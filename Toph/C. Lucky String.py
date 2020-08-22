def dp(string,i,target,count):    
    if i==n:
        return -1
    
    temp = list(string[::])
    temp.sort()
    if temp==target:
        global tempo
        tempo = count    
    
    dp(string+strings[i],i+1,target,count+1)
    dp(string,i+1,target,count)
    
s1 = list(input())
s1.sort()
s2 = list(input())
s2.sort()

n = int(input())

strings = []

tempo = -1
for I in range(n):
    s = input()
    strings.append(s)

dp('',0,s1,0)
first = tempo
tempo = -1
dp('',0,s2,0)
second = tempo


if first==-1 or second==-1:
    print(-1)
else:
    print(first+second)
