from sys import stdout,stdin

#input=stdin.buffer.readline

t = int(input())

for z in range(t):
    n = int(input())
    
    health = []
    explosion = []

    for i in range(n):
        a,b = map(int,input().split())
  
        health.append(a)
        explosion.append(b)

    bullet = max(0,health[0]-explosion[-1])
    health[0]-=max(0,health[0]-explosion[-1])

    for i in range(1,n):
        bullet+=max(0,health[i]-explosion[i-1])
        health[i]-=max(0,health[i]-explosion[i-1])
        
    stdout.write(str(bullet+min(health))+'\n')
