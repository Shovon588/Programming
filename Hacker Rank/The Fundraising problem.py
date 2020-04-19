m,n,t = map(int,input().split())

charm = []
for i in range(m):
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    charm.append((sum(a),a))
