n,k = map(int,input().split())
s = input()

ones = []
for i in range(n):
    if s[i]=='1':
        ones.append(i)

adj = [[] for i in range(n+1)]

for num in ones:
    for i in range(num+1,min(num+k+1,n)):
        if s[i]=='1':
            adj[num].append(i)
            adj[i].append(num)

level = [-1 for i in range(n+1)]

que = [0]
level[0]=0

while len(que)>0:
    cur = que.pop(0)
    
    for node in adj[cur]:
        if level[node]==-1:
            que.append(node)
            level[node]=level[cur]+1

    if level[n-1]!=-1:
        break

print(level[n-1])
