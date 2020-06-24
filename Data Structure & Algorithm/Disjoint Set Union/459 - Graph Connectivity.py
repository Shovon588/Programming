letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def makeset(n):
    par[n] = n

def find(r):
    if par[r] == r:
        return r
    par[r] = find(par[r])
    return find(par[r])

def joint(a,b):
    u = find(a)
    v = find(b)

    if u!=v:
        par[u] = v

def generate_result():
    for i in range(1,n+1):
        temp = find(i)
        if temp in dist:
            pass
        else:
            dist[temp] = "Exist"
    return len(dist)


t = int(input())
s = input()
for I in range(t):
    s = input()    
    n = letters.index(s)+1

    dist = {}
    par = [None]*(n+1)
    for i in range(n+1):
        makeset(i)

    while(1):
        s = input()
        if s=='':break
        a = letters.index(s[0])+1
        b = letters.index(s[1])+1

        joint(a,b)


    print(generate_result())
    if I!=t-1:
        print()




